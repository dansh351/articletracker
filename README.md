Article Tracker is a command line prgram for creating, indexing, and searching bibliographic citations locally. 

I'm sure there are better, fancier versions out there... but if you like no-frills, black coffee versions of things. This one is for you!

**Running the Script**

python3 tracker.py

The main menu will give you the following options: 

1. Create a new article entry
2. Search articles
3. Create Bibliography
4. Exit

**Creating New article entrys**
If you want to Create a new article entry, the next set of prompts will ask you to specify whether the article is a Review, Experimental or Informational article. From there it will ask a specific set of questions for you to summarize the content fo the article. 

It will ask you to specific the directory to save the entry and the entry will be saved as a .txt file in that directory. 

**Searching articles**
If you select Search Articles, it will ask you to specify the directory to search, and then it will ask you to specify what to search for (Title, Author, Keywords)
Once you select your search parameters, it will pull all the relevant articles from your local index and put all the information into one .txt file. 


**Creating Bibliography**
If you select Create Bibliography, it will ask you to specify if you want an Annotated Bibliography or a Works Cited. Both create one big alphabetical bibliography for everything in your local directory based on the APA citation, but the Annotated Bib selection will also include the summary you wrote when creating the citation. 
