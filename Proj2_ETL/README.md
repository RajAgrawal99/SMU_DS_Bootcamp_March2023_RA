# SMU_Project2
The core concept of this project was to create a ETL pipeline to accomplish this we have created 3 jupyter notebooks, their purposes have been outlined below. The schema used to create the tables in postgres can be found in the SQL & ERD folder.

![QuickDBD-Free Diagram](https://github.com/theRobMay/SMU_Project2/assets/90429579/adb68492-9bfb-45c3-a7eb-838da2b953ec)



- The first notebook is the Extration notebook, in this we brought in 2 xlxs files from the resources folder and cleaned the data resulting in 4 new csv files that were then placed back in the resources folder.

- The second is a workbook which takes these new csv files and puts them into a data frame which is then loaded into our schema in postgres SQL using SQL alchemy.

- The third is a workbook which then pulls down the information from our locally hosted postgres SQL and querys it to plot a graph, in this case displaying the most popular catagory of crowdfunded project by total backer count.

![Graph](https://github.com/theRobMay/SMU_Project2/assets/90429579/44f0a967-ffe2-4579-828d-9a07f6ecdd18)

![multiple conditions query](https://github.com/theRobMay/SMU_Project2/assets/90429579/8f1aae12-d6c9-45fa-ad0c-500931aedffe)




  

-Rob & Raj 2023
