from subprocess import call

feats_dir = "/home/jupyter/HatefulMemes/features/feats_hm"

# for each iteration a folder will be created whose name is 'i'
save_dir0 = "save_"

bs = 30

lrs = [1.0, 3.0, 5.0, 7.0, 9.0]

for lr in lrs:
    save_dir = save_dir0 + str(int(lr))
    lr = lr * 1e-5
    rc = call(f"./sweep.sh {save_dir} {bs} {feats_dir} {lr}", shell=True)
