
import os

def save_to_txt(text, file_name="output"):
    
    os.makedirs('./output', exist_ok=True)
    with open(f"./output/{file_name}.txt", mode="w") as f:
        f.write(text)
        f.close()
    print(f"file saved as /output/{file_name}.txt")
    

    
# def save_to_csv(text, file_name="output"):
#     print(f"file saved as /output/{file_name}.txt")
