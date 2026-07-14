def plain_text():
    with open("log.txt","w") as f:
        f.write("Day 2 of comeback \n")
    with open("log.txt","a") as f:
        f.write("File handling review \n")
    with open("log.txt","r") as f:
        print(f.read())

    with open("log.txt","r") as f:
        print(f.readlines())

    with open("log.txt","r") as f:
        for line in f:
            print(line)

if __name__=="__main__":
    plain_text()

import json
config = {"app_name": "MyAI", "version": 1.0, "debug": True, "max_tokens": 500}

def save_config(config,path):
    with open(path,"w") as f:
        json.dump(config,f,indent = 2)


def load_config(path):
    with open(path,"r") as f:
        return(json.load(f))


if __name__ == "__main__":
    save_config(config,"config.json")
    print(load_config("config.json"))
    #assert loaded == config
    print("Round-trip OK")
