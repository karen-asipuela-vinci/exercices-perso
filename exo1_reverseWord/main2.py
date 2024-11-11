#same exo but cleaner
def main():
  print("Write your text: ")
  txt = input()
  txt_reverse = txt[::-1] # [start:stop:step]
  print(txt_reverse)

if __name__ == "__main__":
  main()