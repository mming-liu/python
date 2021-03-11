import os
import pikepdf

class decypt():
    def file_path(path):
        for root,dirs,files in os.walk(path):
        # print(root)     #当前目录路径 
        # print(dirs)     #当前路径下所有子目录 
        # print(files)    #当前路径下所有非目录子文件 
            for file in files:
                if os.path.splitext(file)[1] == '.pdf':
                    filepath = path+file
                return filepath

    def pike_decypt(filepath):
        try :
            with pikepdf.open(filepath,'wb') as pdf:
                # nums = len(pdf.pages)
                # for num in range(0,nums):
                #     if num == 0 or num == nums  :
                #         del pdf.pages[num]
                        pdf.save(filepath)         
            return filepath
        except Exception as e:
            return None 