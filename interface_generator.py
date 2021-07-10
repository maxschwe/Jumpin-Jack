import os
import shutil

try:
    shutil.rmtree("interfaces")
except:
    pass
os.mkdir("interfaces")
for root, dirs, files in os.walk("."):
    for file in files:
        includes_class = False
        if file.split('.')[-1] == "py":
            class_list = []
            text_output = ""
            with open(os.path.join(root, file)) as f:
                text_list = f.read().split("\n")
                for line in text_list:
                    if line.startswith("class"):
                        line = line.replace("class ", "")
                        line = "Klasse " + line
                        class_list.append(line)
                        includes_class = True
                    elif "def " in line:
                        line = line.replace("def","Methode")
                        line = line.replace(":","")
                        class_list.append(line)
            if includes_class:
                text_output = "\n".join(class_list)
                with open(os.path.join("interfaces",file+"_doc"),'w') as f:
                    print(text_output, file)
                    f.write(text_output)