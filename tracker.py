import os
from datetime import datetime

def get_input(prompt):
    return input(prompt).strip()

def save_article(data, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{data['timestamp'].strftime('%Y%m%d%H%M%S')}.txt")
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"Article saved as {filename}")

def create_experimental_entry():
    data = {
        'timestamp': datetime.now(),
        'Title': get_input("Title: "),
        'APA citation': get_input("APA citation: "),
        'Personal rating (1-10)': get_input("Personal rating (1-10): "),
        'Relevant background information': get_input("Relevant background information: "),
        'Research question': get_input("Research question: "),
        'Hypothesis': get_input("Hypothesis: "),
        'Methodology': get_input("Methodology: "),
        'Results': get_input("Results: "),
        'Conclusions': get_input("Conclusions: "),
        'Discussion': get_input("Discussion: "),
        'Thoughts': get_input("What did it make me think of: "),
        'Keywords': get_input("Keywords (comma separated): "),
        'URL/DOI': get_input("URL/DOI: "),
        'Author(s)': get_input("Author(s): "),
        'Journal name': get_input("Journal name: ")
    }
    directory = get_input("Enter the directory to save this entry: ")
    save_article(data, directory)

def create_review_entry():
    data = {
        'timestamp': datetime.now(),
        'Title': get_input("Title: "),
        'APA citation': get_input("APA citation: "),
        'Personal rating (1-10)': get_input("Personal rating (1-10): "),
        'Overview of the topic': get_input("Overview of the topic: "),
        'Main findings': get_input("Main findings: "),
        'Methods reviewed': get_input("Methods reviewed: "),
        'Strengths and weaknesses of the studies': get_input("Strengths and weaknesses of the studies: "),
        'Gaps in the literature': get_input("Gaps in the literature: "),
        'Future research directions': get_input("Future research directions: "),
        'Discussion': get_input("Discussion: "),
        'Thoughts': get_input("What did it make me think of: "),
        'Keywords': get_input("Keywords (comma separated): "),
        'URL/DOI': get_input("URL/DOI: "),
        'Author(s)': get_input("Author(s): "),
        'Journal name': get_input("Journal name: ")
    }
    directory = get_input("Enter the directory to save this entry: ")
    save_article(data, directory)

def create_informational_entry():
    data = {
        'timestamp': datetime.now(),
        'Title': get_input("Title: "),
        'APA citation': get_input("APA citation: "),
        'Personal rating (1-10)': get_input("Personal rating (1-10): "),
        'Summary': get_input("Summary: "),
        'Key points': get_input("Key points: "),
        'Author(s)': get_input("Author(s): "),
        'Publication date': get_input("Publication date: "),
        'Source/Journal': get_input("Source/Journal: "),
        'Relevance/Impact': get_input("Relevance/Impact: "),
        'Personal thoughts': get_input("Personal thoughts: "),
        'Keywords': get_input("Keywords (comma separated): ")
    }
    directory = get_input("Enter the directory to save this entry: ")
    save_article(data, directory)

def create_article_entry():
    article_type = get_input("Enter article type (Experimental, Review, or Informational): ").strip().lower()
    if article_type == 'experimental':
        create_experimental_entry()
    elif article_type == 'review':
        create_review_entry()
    elif article_type == 'informational':
        create_informational_entry()
    else:
        print("Invalid article type. Please try again.")

def search_articles():
    directory = get_input("Enter the directory to search: ")
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    title = get_input("Enter title to search (leave blank to skip): ")
    keyword = get_input("Enter keyword to search (leave blank to skip): ")
    author = get_input("Enter author to search (leave blank to skip): ")
    rating_str = get_input("Enter minimum personal rating (1-10, leave blank to skip): ")
    min_rating = int(rating_str) if rating_str else None
    
    results = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            try:
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(os.path.join(directory, filename), 'r', encoding='iso-8859-1') as file:
                    content = file.read()
                    
            if ((not title or f"Title: {title}" in content) and
                (not keyword or keyword in content) and 
                (not author or f"Author(s): {author}" in content) and 
                (not min_rating or int([line.split(": ")[1] for line in content.split("\n") if "Personal rating" in line][0]) >= min_rating)):
                results.append(content)
    
    if results:
        file_name = get_input("Enter the file name to save the results (with .txt extension): ")
        save_directory = get_input("Enter the directory to save the results: ")
        save_path = os.path.join(save_directory, file_name)
        with open(save_path, 'w', encoding='utf-8') as output_file:
            for result in results:
                output_file.write(result + "\n\n" + "="*40 + "\n\n")
        print(f"Results saved as {save_path}")
    else:
        print("No articles found matching the criteria.")

def create_bibliography():
    directory = get_input("Enter the directory to pull from: ")
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    bibliography_type = get_input("Enter bibliography type (Annotated or Works cited): ").strip().lower()
    
    entries = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            try:
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(os.path.join(directory, filename), 'r', encoding='iso-8859-1') as file:
                    content = file.read()
            if "APA citation: " in content:
                entries.append(content)
    
    if entries:
        entries_sorted = sorted(entries, key=lambda x: x.split("APA citation: ")[1].split("\n")[0])
        
        file_name = get_input("Enter the file name to save the bibliography (with .txt extension): ")
        save_directory = get_input("Enter the directory to save the bibliography: ")
        save_path = os.path.join(save_directory, file_name)
        
        with open(save_path, 'w', encoding='utf-8') as output_file:
            for entry in entries_sorted:
                citation = entry.split("APA citation: ")[1].split("\n")[0]
                output_file.write(citation + "\n")
                if bibliography_type == 'annotated':
                    details = entry.split("APA citation: ")[1].split("\n", 1)[1]
                    output_file.write(details + "\n\n" + "="*40 + "\n\n")
                else:
                    output_file.write("\n")
        
        print(f"Bibliography saved as {save_path}")
    else:
        print("No entries found in the specified directory.")

def main():
    while True:
        choice = get_input("1. Create a new article entry\n2. Search articles\n3. Create Bibliography\n4. Exit\nEnter your choice: ")
        if choice == '1':
            create_article_entry()
        elif choice == '2':
            search_articles()
        elif choice == '3':
            create_bibliography()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
