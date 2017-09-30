#Tyler Reinert- NOTE **I commented out each block of code after I got the answer, then uncommented everything when finished 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#find path of file
dir_path = os.path.dirname(os.path.realpath('wikipedia_traffic.csv'))
#set path of file to a string
filepath = str(dir_path)


#set column width wider
pd.options.display.width = 180

#read csv file, set data types and create dataframe
df = pd.read_csv(filepath + '/wikipedia_traffic.csv', dtype={'langauge': str, 'page_name': str, 'requests': int, 'bytes':int})


#******************************QUESTION 1********************************************************************

#create pivot table to sum requests by language
languages_request = df.pivot_table(index=['language'], values=['requests','bytes'], aggfunc= {'bytes': np.sum, 'requests': np.sum})

#sort by requests in pivot table decending
languages_request.sort_values(by='requests', ascending=False, inplace=True)

#print top 20 most requested
print(languages_request[:20])

#create list with top 20 most requested languages
top_20 = ['en','ja', 'ru', 'de', 'fr', 'es', 'it', 'pl', 'pt', 'zh', 'nl', 'tr', 'sv', 'ar', 'ko', 'uk', 'cs', 'id', 'fi', 'no' ]

#update dataframe to only include languages in top_20 list
df = df[df['language'].isin(top_20)]


#******************************QUESTION 2***********************************************************************

#create new pivot table to figure out median page size
median_pivot = df.pivot_table(index=['language'], values=['requests','bytes'], aggfunc= {'bytes': np.sum, 'requests': np.sum})

#create new column and divide bytes/requests for highest median page size
median_pivot['median_PageSize'] = languages_request['bytes'] / languages_request['requests']


#sort by median page size decending
#median_pivot.sort_values(by='median_Pagesize', ascending=False, inplace=True)

#print pivot table with page sizes
print(median_pivot)


#******************************QUESTION 3****************************************

obama = df['page_name'].str.contains('Obama').sum()
#print(obama)

#create new dataframe for page names containing Obama only
df1 = df[df['page_name'].str.contains('Obama')==True]

#print(df1[:10])


#create new dataframe to sum requests with substring 'Obama'
obama_requests = df1 ['requests'].sum()

print(obama_requests)


#******************************QUESTION 4***********************************************

#create new pivot table and count page names with 'Obama' by langage
obama_languages = df1.pivot_table(index=['language'], values=['page_name'], aggfunc='count')

#order by decending
obama_languages.sort_values(by='page_name', ascending=False, inplace=True)

print(obama_languages)


#******************************QUESTION 5**********************************

#list of english and spanish only
en_and_es = ['en','es']

#update dataframe to include only english and spanish
df = df[df['language'].isin(en_and_es)]


#create new dataframe to find where page names are duplicated
df2 = df[df.duplicated(subset='page_name', keep=False)]

#print(df2[:20])

#find page names that are the same in both english and spanish
same = df2['page_name'].count()


#divide by two since there are two instances of the same page name
print(same/2)


#create pivot table for pages with same name
same_page_name = df2.pivot_table(index=['page_name'], values=['bytes'], aggfunc= 'sum')


#sort by bytes descending
same_page_name.sort_values(by='bytes', ascending=False, inplace=True)

print(same_page_name[:5])


#******************************QUESTION 6***********************************

#update page_name column to remove underscores and replace with spaces 
df['page_name'] = df['page_name'].str.replace('_', ' ')


#create new column that counts the amount of words in the page_name column
df['word_count'] = df['page_name'].str.split().str.len()



#create scatterplot to show relationship between word count and requests 
plt.scatter(df.word_count, df.requests)

#set names for title and x,y axis
plt.title('Number of Request vs. Number of Words in a Page Title')
plt.xlabel('# of Words in Page Title')
plt.ylabel('# of Requests')


plt.show()

















