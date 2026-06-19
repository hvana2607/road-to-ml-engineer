def make_title(text):
    return(f"==={text.title()}===")

def pad_left(test,width):
    s=" "
    return(f"{s*width}{test}")


if __name__=="__main__":
    t = "Hi"
    w=10
    print(f"{make_title(t)}")
    print(f"{pad_left(t,w)}")