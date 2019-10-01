import os
for i in range(1,10):
    os.makedirs(os.path.join('folder', 'subfolder' + str(i)))
