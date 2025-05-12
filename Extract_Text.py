import os

from bs4 import BeautifulSoup

def text_extract(sourceFilePath):
    with open(sourceFilePath, "r", encoding="utf-8") as f:
        html_doc = f.read()


    soup = BeautifulSoup(html_doc, 'html.parser')

    # Find all heading and paragraph elements
    elements = soup.select(
        'h1, article h1, article h2, article h3, article h4, article h5, article h6, article p, article li')

    combined_text = ""

    # Extract and print text from each element
    for element in elements:
        # Using get_text() with parameters for better formatting
        text = element.get_text(' ', strip=True)
        # print(f"{element.name.upper()}: {text}")
        combined_text += text+"\n"

    return combined_text



# Specify directory
directory_name = "Text Extracted Files"


# Specify path
path = f'{directory_name}'

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if (not isExist):
    # Create the directory if folder doesn't exists
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


for root, dirs, files in os.walk("HTML Files"):
    print(f"\nCurrent Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    for dir in dirs:
        
        # Specify path
        folderPath = f'{directory_name}/{dir}'

        # Check whether the specified path exists or not
        isExist = os.path.exists(folderPath)

        if (not isExist):
            # Create the directory if folder doesn't exists
            try:
                os.mkdir(folderPath)
                print(f"Directory '{folderPath}' created successfully.")
            except PermissionError:
                print(f"Permission denied: Unable to create '{folderPath}'.")
            except Exception as e:
                print(f"An error occurred: {e}")
        
    for file in files:
        fileName=os.path.splitext(file)[0]
        sourceFilePath=f"{root}\{file}"
        # print(sourceFilePath)
        destinationFilePath=f"{directory_name}/{root.split('\\')[1]}/{fileName}.txt"
        text=text_extract(sourceFilePath)
        with open(destinationFilePath,"w",encoding="utf-8") as f:
            f.write(text)
        
            
            
        