import sys
import re
import os
import fnmatch
import time
import string
from os.path import getsize
from sys import platform as _platform
from os import rename, listdir
from os import walk
from stat import S_ISREG, ST_CTIME, ST_MODE


class bulk_tool_change:
  def __init__(self):
     self.path=input("please enter the location of the directory")  
     if os.path.isdir(self.path):  
          print("\nIt is a directory")  
     elif os.path.isfile(self.path):  
          print("\n Not a directory but is a normal file")  
     else:  
       print("WRONG!,ERROR!! no such directory exists!! or it could be a special file(FIFO,SOCKET ETC)")
       main()

  def store_files(self):
     files= []
     for (dirpath, dirnames, filenames) in walk(self.path):
         files.extend(filenames)
         break
     if(len(files)==0):
         print("The directory has no files in there")
         main()
     return files

  
            
           

  
  def renameFile(self,filename,rename,i):
            filename_without_ext = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            new_file_name = rename + str(i)
            new_file_name_with_ext = new_file_name+extension
            print(new_file_name_with_ext)
            os.rename(os.path.join(self.path,filename),os.path.join(self.path,new_file_name_with_ext))
  def stringFun(self):
            rename = input("Enter the named convention")
            if ((_platform == "linux") and ('/' in changename)):
               print("in linux platform file name should not contain a /")
            elif((_platform == "darwin") and (':' in changename)):
               print("in MAC OS platform file name should not contain a :")
            if(('*' in changename)or('<' in changename)or('>' in changename)or('?'in changename)or('/'in changename)or('\\' in changename)or('|' in changename)or(':' in changename)):
               print("Filename shouldnot contain *<>?/\|:")
            if(('*' in rename)or('<' in rename)or('>' in rename)or('?'in rename)or('/'in rename)or('\\' in rename)or('|' in rename)or(':' in rename)):
                  print("Filename shouldnot contain *<>?/\|:")
                  main()
            
            i = 1 
            for filename in os.listdir(self.path) :
                  if((self.path + "/" + filename) == sys.argv[0]):
                        continue 
                  self.renameFile(filename,rename,i)
                  i += 1

  def change_for_x():
     rename =input("Enter the name convention.Filename shouldnot contain *<>?/\|:")
     num = int(input("Enter no of files to be renamed"))
     i = 1 
     for filename in sort_file :
     if(i > num) :
       break 
     self.renameFile(filename,rename,i)
     i += 1

    




  def remove_double_prefix(self):
    files = self.store_files()
    badprefix=input("enter the prefix to be removed")
    for fname in files:
        if fname.startswith(badprefix*2):
            rename(fname,fname.replace(badprefix,'',1))
            print(fname)
            




  def change_prefix(self):
    prefix=input("enter the prefix to change")
    change=input("enter the one to which you want to change")
    fnames=listdir('.')
    for fname in fnames:
        if fname.startswith(prefix):
            rename(fname,fname.replace(prefix,change,1))
            print(fname)
            


# replace file name with a word and sequentially number all the files
  def sequential_number(self):
    files = self.store_files()
    filenumber=int(input("enter the number you want to start with"))
    replace=input("enter the one to which you want to change")
    extention = self.path.split('/')[-1]

    for filename in  files:
      os.rename(self.path +'\\'+ filename,self.path + '\\'+"replace" + str(filenumber)+"extention")
      filenumber +=1
      print(filename)


# rename all files into uppercase
  def all_upper(self):
    files = self.store_files()
    for f in files:
        newname=f.upper()
        if newname == f:
            continue
        if newname in files:
            print( "error: %s already exists" % newname )
        f=f+1
    os.rename(f, newname)
    print(newname)


#rename all files to lowercase
  def all_lower(self):
    files = self.store_files()
    for f in files:
        newname=f.lower()
        if newname == f:
            continue
        if newname in files:
            print( "error: %s already exists" % newname )
        f=f+1
    os.rename(f, newname)
    print(newname)


#sort a few files alphabetically in ascending order
  def sort_ascending(self):
    files = self.store_files()
    sorted_file = sorted(files,reverse = False)
    print("The files are :")
    for i in  sorted_file:
      print(i)
    self.change_for_x(sort_file)


#sort all files in ascending
  def sort_ascending_all(self):
    files = self.store_files()
    sorted_ascending = sorted(files,reverse = False)
    print("The files are :")
    for i in  sorted_ascending:
      print(i)
    
    



#sort a few files alphabetically in descending order
  def sort_descending(self):
    files = self.store_files()
    sorted_file = sorted(files,reverse = True)
    print("The files are :")
    for i in  sorted_file:
      print(i)
    self.change_for_x(sort_file)
   


#sort all files in desscending
  def sort_descending_all(self):
    files = self.store_files()
    sorted_descending = sorted(files,reverse = True)
    print("The files are :")
    for i in  sorted_descending:
      print(i)
    

    



#sort all files ascending order by size:
  def sort_ascending_size(self):
    files = self.store_files()
    size_ascending = sorted(files,key=getsize,reverse = False)
    print("The files are :")
    for x in size_ascending:
        print(x)
    self.change_for_x(files)


#sort all files descending order by size:
  def sort_descending_size(self):
    files = self.store_files()
    size_descending = sorted(files,key=getsize,reverse = True)
    print("The files are :")
    for y in size_descending:
        print(y)
    
    
    


#change spaces to hypens and all letters to lowercase in all files
  def change1(self):
    
    files = self.store_files()
    filenames = os.listdir(self.path)
    for filename in files:
       os.rename(filename, filename.replace(" ", "-").lower())
       print(filenames)
    
    


#change spaces to ** and all letters to uppercase
  def change2(self): 
    files = self.store_files()
    filenames = os.listdir(self.path) 
    for filename in filenames:
       os.rename(filename, filename.replace(" ", "**").upper())
       print(filenames)
    
    


#rename all files in a folder by a word and sequential numbering thereafter:
  def word_change(self): 
    path=self.path
    filenames = os.listdir(path) 
    word =input("enter word you want")
    for count, filename in enumerate(os.listdir("path")): 
        dst ="word" + str(count) + "extension"
        src ='path'+ filename 
        dst ='path'+ dst 
        os.rename(src, dst) 
        print(filenames)
    self.change_for_x(filenames)
    
   



#directory listing, sorted by creation date.
  def date_sort(self):
    files = self.store_files()
    dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)

    data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data):
        print(time.ctime(cdate), os.path.basename(path))
    
    


#to remove . and replace by _ :
  def change3(self):
    filenames = os.listdir(self.path)
    for filename in filenames:
      os.rename(filename, filename.replace(".", "_").lower())
      print(filename)




#to remove all numbers from a filename in a directory:
  def remove_numbers(self):
    filenames1 = os.listdir(self.path)
    saved_path=os.getcwd()
    print("Current Working Directory Is " +saved_path)
    os.chdir(r"file")
    for file_name in filenames1:
          os.rename(file_name, file_name.translate(None, '0123456789'))
    os.chdir(saved_path)
    print(file_name)






def main():
       obj=bulk_tool_change()

       to_choose=input("please enter your choice \n 1.if the file name has two prefix like deepti_deepti, remove one prefix \n 2.if prefix has to be changed \n 3.replace file name with a word and sequentially number all the files \n 4.rename all files into uppercase \n 5.rename all files into lowercase \n 6.sort all files alphabetically in ascending order \n 7.sort all files alphabetically in desscending order \n 8.sort all files ascending order by size: \n 9.sort all files descending order by size \n 10.change spaces to hypens and all letters to lowercase \n 11.change spaces to ** and all letters to uppercase \n 12.rename all files in a folder by a word and sequential numbering thereafter \n 13.directory listing, sorted by creation date. \n 14.to remove . and replace by _  \n 15. remove all the number occurances in a filename \n 16.sort only x files ascneding  \n 17. sort only x files descending")
 

       if(to_choose == '1'):
          obj.remove_double_prefix()
         
       elif (to_choose == '2'):
          obj.change_prefix()
         
       elif (to_choose == '3'):
          obj.sequential_number()
         
       elif (to_choose == '4'):
          obj.all_upper()
         
       elif (to_choose == '5'):
          obj.all_lower()
 
       elif(to_choose == '6'):
          obj.sort_ascending_all()
         
       elif(to_choose == '7'):
          obj.sort_descending_all()
         
       elif (to_choose == '8'):
          obj.sort_ascending_size()
        
       elif(to_choose == '9'):
          obj.sort_descending_size()
        
       elif(to_choose == '10'):
          obj.change1()

       elif(to_choose == '11'):
          obj.change2()

       elif(to_choose == '12'):
          obj.word_change()

       elif(to_choose == '13'):
          obj.date_sort()

       elif(to_choose == '14'):
          obj.change3()

       elif(to_choose == '15'):
          obj.remove_numbers()
       
       elif(to_choose == '16'):
          obj.sort_ascending()

       elif(to_choose == '17'):
          obj.sort_descending()


     

if __name__ == "__main__":
        main()


     

    
        

        
   








	
  





  





















    
            




   












