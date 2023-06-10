import json_lines
import csv
import numpy as np
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score
import matplotlib.pyplot as plt

INPUT_FILE = 'dev_unseen.jsonl'

true_labels = []
with open(INPUT_FILE, 'rb') as f:
    for item in json_lines.reader(f):
        true_labels.append(item['label'])

# print(true_labels)
# print(len(true_labels))

# a list of 27 sublists, each containing 540 predictions from a model
model_predictions = np.zeros((27, 540, 3), dtype='object')

for i in range(27):
    with open('./predict/' + str(i) + '.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        pred = []
        for row in reader:
            if row:
                pred.append(row)
        model_predictions[i] = pred[1:]

# print(model_predictions)
# print(len(model_predictions))

model_predictions = np.array(model_predictions)
model_predictions[:, :, 1] = model_predictions[:, :, 1].astype(float)
model_predictions[:, :, 2] = model_predictions[:, :, 2].astype(int)
# print(model_predictions[0][:, 1])
# print(model_predictions[0][:, 2])

acc_total = 0
models_acc = {}
models_f1 = {}
models_auroc = {}
majority_voting_count = np.zeros((540, ), dtype=int)

for i in range(27):

    pred_labels = list(model_predictions[i][:, 2])

    # Accuracy
    acc = accuracy_score(true_labels, pred_labels)

    # F1
    # In classification tasks for which every test case is guaranteed to be assigned to exactly one class, micro-F1 is equivalent to accuracy.
    f1 = f1_score(true_labels, pred_labels, average='weighted') # take label imbalance into account

    # AUROC
    auroc = roc_auc_score(true_labels, pred_labels, average='weighted') # take label imbalance into account

    models_acc[i] = acc
    models_f1[i] = f1
    models_auroc[i] = auroc
    majority_voting_count = majority_voting_count + model_predictions[i][:, 2]

# print("Avg acc: ", acc_total / 27)  0.72!
# print(sorted(models_acc.items(), key=lambda x: x[1], reverse=True))
# print(sorted(models_f1.items(), key=lambda x: x[1], reverse=True))
# print(sorted(models_auroc.items(), key=lambda x: x[1], reverse=True))
# print(majority_voting_count)


majority_voting_count[majority_voting_count <= 13] = 0
majority_voting_count[majority_voting_count > 13] = 1
# print(majority_voting_count)

# Majority voting accuracy and AUROC
majority_voting_acc = accuracy_score(true_labels, list(majority_voting_count))
majority_voting_AUROC = roc_auc_score(true_labels, list(majority_voting_count), average='weighted')
print("\nMajority Voting Accuracy: ", majority_voting_acc)  # 0.7351851851851852
print("Majority Voting AUROC: ", majority_voting_AUROC)  # 0.6847058823529412


ranked_by_acc = np.array(sorted(models_acc.items(), key=lambda x: x[1], reverse=True), dtype=int)[:, 0]
# print(ranked_by_acc)
ranked_by_auroc = np.array(sorted(models_auroc.items(), key=lambda x: x[1], reverse=True), dtype=int)[:, 0]

# Weighted voting accuracy and AUROC
DECAY_ENDs = [i / 10 for i in range(1, 11)]
weighted_AUROC_ranked_by_acc = []
weighted_acc_ranked_by_acc = []
weighted_AUROC_ranked_by_AUROC = []
weighted_acc_ranked_by_AUROC = []
simple_avg_AUROC_ranked_by_acc = []
simple_avg_acc_ranked_by_acc = []
simple_avg_AUROC_ranked_by_AUROC = []
simple_avg_acc_ranked_by_AUROC = []

for DECAY_END in DECAY_ENDs:

    DECAY = DECAY_END ** (1.0 / 27)
    print("\nDECAY_END: ", DECAY_END)
    print("DECAY: ", DECAY)

    factor_sum = 0
    for i in range(27):
        factor = DECAY ** i
        factor_sum += factor

    print("Factor Sum: ", factor_sum)

    weighted_voting_pred_acc = np.zeros((540, ))
    weighted_voting_pred_AUROC = np.zeros((540, ))



    for i in range(27):
        model_pred_probs = model_predictions[i][:, 1]
        ranking_acc = np.where(ranked_by_acc == i)[0][0]
        factor_acc = DECAY ** ranking_acc
        weighted_voting_pred_acc = weighted_voting_pred_acc + model_pred_probs * (factor_acc / factor_sum)

        ranking_AUROC = np.where(ranked_by_auroc == i)[0][0]
        factor_AUROC = DECAY ** ranking_AUROC
        weighted_voting_pred_AUROC = weighted_voting_pred_AUROC + model_pred_probs * (factor_AUROC / factor_sum)

    weighted_voting_pred_acc[weighted_voting_pred_acc <= 0.5] = 0
    weighted_voting_pred_acc[weighted_voting_pred_acc > 0.5] = 1
    weighted_voting_pred_AUROC[weighted_voting_pred_AUROC <= 0.5] = 0
    weighted_voting_pred_AUROC[weighted_voting_pred_AUROC > 0.5] = 1
    weighted_AUROC_ranked_by_acc.append(roc_auc_score(true_labels, list(weighted_voting_pred_acc)))
    weighted_acc_ranked_by_acc.append(accuracy_score(true_labels, list(weighted_voting_pred_acc)))
    print("weighted AUROC ranked by acc: ", weighted_acc_ranked_by_acc[-1])
    print("weighted Accruacy ranked by acc: ", weighted_AUROC_ranked_by_acc[-1])
    weighted_AUROC_ranked_by_AUROC.append(roc_auc_score(true_labels, list(weighted_voting_pred_AUROC)))
    weighted_acc_ranked_by_AUROC.append(accuracy_score(true_labels, list(weighted_voting_pred_AUROC)))
    print("weighted AUROC ranked by AUROC: ", weighted_acc_ranked_by_AUROC[-1])
    print("weighted Accruacy ranked by AUROC: ", weighted_AUROC_ranked_by_AUROC[-1])


for k in range(27):
    print("\nTop ", k+1)
    top_k_acc = ranked_by_acc[:k]
    top_k_AUROC = ranked_by_auroc[:k]

    avg_voting_pred_acc = np.zeros((540, ))
    avg_voting_pred_AUROC = np.zeros((540, ))
    for i in top_k_acc:
        avg_voting_pred_acc = avg_voting_pred_acc + model_predictions[i][:, 1]

    avg_voting_pred_acc[avg_voting_pred_acc <= 0.5] = 0
    avg_voting_pred_acc[avg_voting_pred_acc > 0.5] = 1
    simple_avg_AUROC_ranked_by_acc.append(roc_auc_score(true_labels, list(avg_voting_pred_acc)))
    simple_avg_acc_ranked_by_acc.append(accuracy_score(true_labels, list(avg_voting_pred_acc)))
    print("Simple Avg AUROC ranked by acc: ", simple_avg_AUROC_ranked_by_acc[-1])
    print("Simple Avg Accruacy ranked by acc: ", simple_avg_acc_ranked_by_acc[-1])


    for j in top_k_AUROC:
        avg_voting_pred_AUROC = avg_voting_pred_AUROC + model_predictions[j][:, 1]

    avg_voting_pred_AUROC[avg_voting_pred_AUROC <= 0.5] = 0
    avg_voting_pred_AUROC[avg_voting_pred_AUROC > 0.5] = 1
    simple_avg_AUROC_ranked_by_AUROC.append(roc_auc_score(true_labels, list(avg_voting_pred_AUROC)))
    simple_avg_acc_ranked_by_AUROC.append(accuracy_score(true_labels, list(avg_voting_pred_AUROC)))
    print("Simple Avg AUROC ranked by AUROC: ", simple_avg_AUROC_ranked_by_AUROC[-1])
    print("Simple Avg Accuracy ranked by AUROC: ", simple_avg_acc_ranked_by_AUROC[-1])


# Plot Weighted AUROC and Acc with Weighted Voting
plt.title("AUROC & Accuracy by Weighted Voting on dev_unseen")
plt.xlabel("Decay End")
plt.ylabel("Scores")
plt.grid()
plt.plot(DECAY_ENDs, weighted_AUROC_ranked_by_acc, label="Weighted Voting AUROC ranked by acc")
plt.plot(DECAY_ENDs, weighted_acc_ranked_by_acc, label="Weighted Voting Accuracy ranked by acc")
plt.plot(DECAY_ENDs, weighted_AUROC_ranked_by_AUROC, label="Weighted Voting AUROC ranked by AUROC")
plt.plot(DECAY_ENDs, weighted_acc_ranked_by_AUROC, label="Weighted Voting Accuracy ranked by AUROC")
plt.hlines(y=majority_voting_AUROC, xmin=0.1, xmax=1.0,  color='purple', linestyle='dashed',label='Majority Voting AUROC')
plt.hlines(y=majority_voting_acc, xmin=0.1, xmax=1.0,  color='yellow', linestyle='dashed',label='Majority Voting Accuracy')
plt.legend()
plt.savefig("weighted_scores.png")
plt.close()


# Plot Weighted AUROC and Acc with Average Voting
Top_K = [i for i in range(1, 21)]
plt.title("AUROC & Accuracy by Simple Averaging on dev_unseen")
plt.xlabel("Top K Models")
plt.ylabel("Scores")
plt.grid()
plt.plot(Top_K, simple_avg_AUROC_ranked_by_acc[:20], label="Simple Averaging AUROC ranked by acc")
plt.plot(Top_K, simple_avg_acc_ranked_by_acc[:20], label="Simple Averaging Accuracy ranked by acc")
plt.plot(Top_K, simple_avg_AUROC_ranked_by_AUROC[:20], label="Simple Averaging AUROC ranked by AUROC")
plt.plot(Top_K, simple_avg_acc_ranked_by_AUROC[:20], label="Simple Averaging Accuracy ranked by AUROC")
plt.hlines(y=majority_voting_AUROC, xmin=1, xmax=20,  color='purple', linestyle='dashed',label='Majority Voting AUROC')
plt.hlines(y=majority_voting_acc, xmin=1, xmax=20,  color='yellow', linestyle='dashed',label='Majority Voting Accuracy')
plt.legend()
plt.savefig("simple_avg_scores.png")
plt.close()