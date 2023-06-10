Last login: Thu May  6 10:10:11 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
YiWangs-MacBook-Air:~ yiwang$ conda activate cv_proj
cd (cv_proj) YiWangs-MacBook-Air:~ yiwang$ cd /Users/yiwang/Documents/Courses/OMSCS/7643DeepLearning/groroject/
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ ls
2012.12975.pdf                  figlr.pdf
Group_Project_Description-1.pdf pltlr.py
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ python pltlr.py 
save  ./figlr.pdf
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ python pltlr.py 
Traceback (most recent call last):
  File "pltlr.py", line 35, in <module>
    ax.set_xticklabels(fontsize=20)
TypeError: set_xticklabels() missing 1 required positional argument: 'labels'
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ python pltlr.py 
save  ./figlr.pdf
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ python pltlr.py 
save  ./figlr.pdf
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ ls
2012.12975.pdf                  figlrv2.pdf
Group_Project_Description-1.pdf pltlr.py
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ pwd
/Users/yiwang/Documents/Courses/OMSCS/7643DeepLearning/groupProject
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ ls
2012.12975.pdf                  figlrv2.pdf
Group_Project_Description-1.pdf pltlr.py
(cv_proj) YiWangs-MacBook-Air:groupProject yiwang$ vi pltlr.py 







data0 = [0.73375,0.717735,0.722261,0.646294,0.62604]

data1 = [0.7320,0.7063,0.7081,0.5770,0.5234]

x = [1,3,5,7,9]

fig = plt.figure(figsize=(6.1,5))
ax=fig.add_subplot(111)

ax.plot(x,data0, marker='<', c='black', label = 'best')
ax.plot(x,data1, marker='o', c='black', label = 'final')

ax.legend(fontsize=24,loc=3)
#cb.set_ticks(np.linspace(hb.get_array().min(), hb.get_array().max(), 6))
#cb.set_ticklabels(np.linspace(0, 1., 6))
#cb.set_label('Normalized Count', fontsize=16)
#cb.ax.tick_params(labelsize=16)

#ax.set_title('H2SO4 particle (Number Concentration: '+r' 10$^2 g/m^3$)', fontsize=16)
#ax.set_xlabel('Particle radius ('+'$\mu$'+'m)', fontsize=16)
ax.set_ylabel('AUC', fontsize=26)

ax.set_xlabel('Learning rate (*1e-5)', fontsize=26)
#ax42.set_ylabel('Normalized Frequency', fontsize=10)
#ax.set_title('Two Hibit model (THM)', fontsize=16)
ax.set_xlim(0,9.3)
ax.set_ylim(0.5,0.9)
#ax.set_xticklabels(fontsize=20)
ax.tick_params(labelsize=20)
ax.set_xticks([0,1,3,5,7,9])
ax.set_yticks([0.5,0.6,0.7,0.8,0.9])

pngname = "./"+"figlr"+".pdf"
print("save ", pngname)
plt.savefig(pngname, dpi=50, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches='tight', pad_inches=0.1)

plt.show()


