import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

class Sales_Data_Analyzer:
   def __init__(self):
      self.data = None
      self.data1 = None
      self.table = None
      self.merge1 = None

   def Load_Data(self,path):
      
      self.data = pd.read_csv(path)
      if "OrderDate" in self.data.columns:
         self.data['OrderDate']=pd.to_datetime(self.data['OrderDate'],format="%d-%m-%Y")
         
         self.data["Month"] = self.data['OrderDate'].dt.month
         self.data["Year"] = self.data['OrderDate'].dt.year
         self.data["Dates"] = self.data['OrderDate'].dt.day
      

   def Explore_Data(self):
      while True:
        print("1. Display The First 5 Rows")
        print("2. Display The Last 5 Rows")
        print("3. Display column Name")
        print("4. Display Data Type")
        print("5. Display Basic Info")
        print("6. Exit")

        try:
            ch1 = int(input("Enter Your Choice"))

            match ch1:
                case 1:
                    print("===Display The First 5 Rows===")
                    try:
                     print(self.data.head())
                     print()
                    except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                       
                    
                case 2:
                    print("===Display The Last 5 Rows===")
                    try:
                     print(self.data.tail())
                     print()
                    except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                       
                case 3:
                    print("===Display column Name===")
                    try:
                     print(self.data.columns)
                     print()
                    except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                       
                case 4:
                    print("===Display Data Type===")
                    try:
                     print(self.data.dtypes)
                     print()
                    except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                       
                case 5:
                    print("===Display Basic Info===")
                    try:
                     print(self.data.info())
                     print()
                    except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                       
                case 6:
                    break
                case _:
                    print()
                    print("Invalid Input....") 
                    print()                  
        except ValueError:
                print()
                print("Invalid Input...")  
                print()


   def Clean_Data(self):
      while True:
         print("1. Display Rows With Missing Values")
         print("2. Fill Missing Values With Mean")
         print("3. Drop Rows With Missing Values")
         print("4. Replace Missing Values With A Specific Value")
         print("5. Exit")

         try:
            ch1 = int(input("Enter Your Choice"))
            
            match ch1: 
               case 1:
                  print("===Display Rows With Missing Values===")
                  try:
                     print(self.data.isnull().sum())
                     print()
                  except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                     
               case 2:
                  print("===Fill Missing Values With Mean===")
                  try:
                     r = input("Enter Your Column Name Only Numeric ")
                     if r in self.data.columns:
                        self.data[r] = self.data[r].fillna(self.data[r].mean())
                        print(self.data.isnull().sum())
                        print()
                     else:
                        print("Invalid Column Name")   
                  except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                     
               case 3:
                   print("===Drop Column With Missing Values===")
                   try:
                     r = input("Enter Your Column Name")
                     if r in self.data.columns:
                        self.data.drop([r],axis=1,inplace=True)
                        print(self.data.isnull().sum())
                        print()
                     else:
                        print("Invalid Column Name")   
                   except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
               
               case 4:
                  print("===Replace Missing Values With A Specific Value===")
                  try:
                     r = input("Enter Your Column Name")
                     v = input("Enter Your Replace Value")
                     if r in self.data.columns:
                        self.data[r] = self.data[r].fillna(v)
                        print(self.data.isnull().sum())
                        print()
                     else:
                        print("Invalid Column Name")   
                  except AttributeError:
                       print()
                       print("Please LoadData....") 
                       break
                  
               case 5:  
                  break     
               case _:
                  print()
                  print("Invalid Input...")
                  print()

         except ValueError:
            print()
            print("Invalid Input....")
            print()   


   def Mathematical_Operations(self): 
      while True:
         print("===Perform DataFrame Operations===")
         print()
         print("1. Aggregate And Statistical  Data")
         print("2. Split Data")
         print("3. Search And Sort Data")
         print("4. Filter Data")
         print("5. Indexing Data")
         print("6. Exit")
         
         try:

            ch1 = int(input("Enter Your Choice"))

            match ch1:
               case 1:
                  print("===Aggregate And Statistical Data===")
                  self.Aggregation_And_Statistical()
               case 2:
                  print("===Split Data===") 
                  self.Split_Data()

               case 3:
                  print("===Search And Sort Data===")
                  self.Search_Sort_Data()
               case 4:
                  print("===Filter Data===")
                  self.Filter_Data()
               case 5:
                  print("===Indexing Data===")
                  self.Indexing_Data()

               case 6:
                  print()
                  break                    
               case _:
                  print("Invalid Input....")
                       
         except ValueError:
            print()
            print("Invalid Data...")
            print()   


   def Split_Data(self) :
      try:
         col = input("Enter Your Column Name")
         if col in self.data.columns:
            qty=self.data[col].to_numpy()
            print(qty)
            s = int(input("Enter Your Spliting Size"))
            if s > 0:
               print(np.array_split(qty, s))
            else:
               print("Invalid Input")  
         else:
                        print("Invalid Column Name")       
         print()
      except AttributeError:
            print()
            print("Please LoadData....") 
            print()

   def Indexing_Data(self) :
      try:
         col = input("Enter Your Column Name")
         if col in self.data.columns:
            qty=self.data[col].to_numpy()
            print(qty)
            s = int(input("Enter Your Start Index Number"))
            e1 = int(input("Enter Your Ending Indext Number"))
            if s < e1:
               print(qty[s:e1])
            else:
               print("Invalid Input")   
         else:
            print("Invalid Column Name")      
         print()
      except AttributeError:
            print()
            print("Please LoadData....") 
            print()  


   def Search_Sort_Data(self):
         while True:
            print("1  Sort Data Ascending")
            print("2. Sort Data Desecding")
            print("3. Search Value")
            print("4. Exit")

            try:
              ch = int(input("Enter Your Choice"))

              match ch :
                 case 1:
                    print("Sort Data Ascending")

                    try:
                        col = input("Enter Your Column Name ")
                        if col in self.data.columns:
                           qty=self.data[col].to_numpy()
                           print(qty)
                           index = np.sort(qty)
                           print(index)
                           
                           print()
                        else:
                         print("Invalid Columnes Name")   
                    except AttributeError:
                        print()
                        print("Please LoadData....")    
                 case 2:
                    print("Sort Data Descending") 

                    try:
                        col = input("Enter Your Column Name  ")
                        if col in self.data.columns:
                           qty=self.data[col].to_numpy()
                           print(qty)
                           index = np.sort(qty,)[::-1]
                           print(index)
                           
                           print()
                        else:
                         print("Invalid Columnes Name")   
                    except AttributeError:
                        print()
                        print("Please LoadData....")   
                 case 3:
                     try:
                        col = input("Enter Your Column Name only Numeric ")
                        if col in self.data.columns:
                           qty=self.data[col].to_numpy()
                           print(qty)
                           a = int(input("Enter Your Searching Value"))
                           index = np.where(np.isclose(qty ,a))[0]

                           if len(index) > 0:
                              print(f"{a} found at index positions: {list(index)}")
                           else:
                              print(f"{a} not found")

                           print()
                        else:
                         print("Invalid Columnes Name")   
                     except AttributeError:
                        print()
                        print("Please LoadData....")             
                 case 4:
                    break
                 case _:
                    print()
                    print("Invalid Input...")
                    print()
                             
            except ValueError:
               print()
               print("Invalid Input")
               print()   


         

            
   def Aggregation_And_Statistical(self):
      try:
         col = input("Enter Your Column Name Only Give Numeric Column")
         if col in self.data.columns:
            qty=self.data[col].to_numpy()
            arr = np.array(qty)
            print(qty)
            while True:
               print("1. Sum")
               print("2. Mean")
               print("3. shape")
               print("4. type")
               print("5. std")
               print("6. variance")
               print("7. count")
               print("8. Percentitiles")
               print("9.Exit")
            
               try:
                  
                  ch = int(input("Enter Your Choice"))

                  match ch:
                     case 1:
                        print("Sum is:",np.sum(arr))
                     case 2:
                        print("Mean Is",np.mean(arr))
                     case 3:
                        print("Shape of Array",arr.shape)
                     case 4:
                        print("Data Type",arr.dtype) 
                     case 5:
                        print("Standard Deviation",np.std(qty))
                     case 6:
                        print("Variance of Array",arr.var())
                     case 7:
                        print("Count",np.size(arr))
                     case 8:
                        a = int(input("Enter Your Percentiles [0-100]"))
                        print("percentiles",np.percentile(arr,a)) 
                     case 9:
                        break
                     case _:
                        print()
                        print("Invalid Input....")
                        print()  
                                         

               except ValueError:
                  print()
                  print("Invalid Input...")   
                  print()
         else:
            print("Invalid Column Name")         
            
         print()
      except AttributeError:
            print()
            print("Please LoadData....") 
            print()  

   def Filter_Data(self):
      try:
         if "OrderDate" in self.data.columns:
               
               self.data['OrderDate']=pd.to_datetime(self.data['OrderDate'],format="%d-%m-%Y")
         
               self.data["Month"] = self.data['OrderDate'].dt.month
               self.data["Year"] = self.data['OrderDate'].dt.year
               self.data["Dates"] = self.data['OrderDate'].dt.day
                     
               print(self.data.head(2))

               col = input("Enter Your Column ")
               m = input("Enter Your Month [YYYY-MM]")

               d = self.data["OrderDate"].to_numpy()
               c = self.data[col].to_numpy()

               

               check = d.astype('datetime64[M]') == np.datetime64(m)   

               res = np.column_stack((d,c))  
               print(res[check])

         else:
            print("Your Data In Not OrderDate Column")
       

      except AttributeError:
            print()
            print("Please LoadData...")
            print()  

   def Generate_Descriptive_Statistics(self):
      while True:
         print("===Generate Descriptive Statistics===")
         print("1. Combine Data")
         print("2. Pivot Table")
         print("3. Exit")
         try:
            ch = int(input("Enter Your Choice"))

            match ch :
               case 1:
                  print("===Combine Data===")
                  self.Combine_Data()
               case 2:
                  print("===Pivot Table===")
                  self.Create_Pivot_Table()             
               case 3:
                   break
               case _:
                  print()
                  print("Invalid Input...")
                  print()            
         except ValueError:
            print()
            print("Invalid Input...")
            print()            


   def Combine_Data(self):
      try:
         path = input("Enter Your Path Other File")
         self.data1 = pd.read_csv(path)
         self.merge1 = pd.merge(self.data,self.data1,how="inner",on="OrderID")
         self.data = self.merge1
         print(pd.merge(self.data,self.data1,how="inner",on="OrderID")) 
      except AttributeError:
         print()
         print("Please LoadData....")
         print()

   def Create_Pivot_Table(self):
      try:
         i1 = None
         v1= None
         a1 = None
         print(self.data.head(2))

         i1 = input("Enter Your Index")
         v1 = input("Enter Your Values")
         a1 = input("Enter Your aggfunc like [mean,sum,count]")

         if i1 in self.data.columns and v1 in self.data.columns:
           print()
           self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1)
           print(self.table)
         elif i1 in self.merge1.columns and v1 in self.merge1.columns:  
            self.table = self.merge1.pivot_table(index=i1,values=v1,aggfunc=a1)
            print(self.table)
         else:
            print("Invalid Column Name")  

      except AttributeError:
         print()
         print("Please LoadData...")
         print()





class Visualiztion(Sales_Data_Analyzer):
   def __init__(self):
      super().__init__()
      self.save = []


   def Load_Data(self, path):
      return super().Load_Data(path)  
   
   def SaveVisualize_Data(self):
      f = input("Enter Your image Name [image.png/jpg]")
      plt.savefig(f,bbox_inches="tight")
      print(f"Plot saved successfully as {f}")
      
   
   
   def bar_plot(self):
      try:
         print(self.data.head(2))
         ask =input("If You Create Pivot Table (yes/no)").lower()

         if ask == "yes":

             i1 = None
             v1= None
             a1 = None
         
             i1 = input("Enter Your Index")
             v1 = input("Enter Your Values")
             a1 = input("Enter Your aggfunc like [mean,sum,count]")

             if i1 in self.data.columns and v1 in self.data.columns:
               print()
               self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1).reset_index()
               print(self.table)

               sns.barplot(data=self.table,x=i1,y=v1,color="green")
               plt.legend([i1])
               plt.title(f"{i1} by {v1}")
               plt.xlabel(f'{i1}')
               plt.ylabel(f'{v1}')
               plt.xticks(rotation=45,ha="right")
               self.SaveVisualize_Data()
               plt.show()
               print("Bar Plot Creeate.....")
               print("Display The Bar Plot...")
               print("Save image...")
               print()
             else:
                print("Invalid Column Name")  

         else:
            x = input("Enter X-axis Column Name:")
            y = input("Enter Y-axis column Name")
            hue = input("Enter Your hue perameter")

            hue = hue if hue.strip() in self.data.columns else None

            if x in self.data.columns and y in self.data.columns:
               sns.barplot(data=self.data,x=x,y=y,hue=hue)
               plt.title(f"{x} by {y}")
               plt.xlabel(f'{x}')
               plt.ylabel(f'{y}')
               plt.xticks(rotation=45,ha="right")
               self.SaveVisualize_Data()
               plt.show()
               print("Bar Plot Creeate.....")
               print("Display The Bar Plot...")
               print("Save image...")
               print()
            else:
               print("Invalid Column Name")   
      except AttributeError:
         print()
         print("Please LoadData....")
         print()   


   def Line_plot(self):
      try:
         print(self.data.head(2))
         ask =input("If You Create Pivot Table (yes/no)").lower()

         if ask == "yes":

             i1 = None
             v1= None
             a1 = None
         
             i1 = input("Enter Your Index")
             v1 = input("Enter Your Values")
             a1 = input("Enter Your aggfunc like [mean,sum,count]")

             if i1 in self.data.columns and v1 in self.data.columns:
               print()
               self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1).reset_index().sort_values(ascending=True,by=i1)
               print(self.table)

               plt.plot(self.table[i1],self.table[v1],label=v1,marker="o",color="green")
               plt.title(f"{i1} by {v1}")
               plt.xlabel(f'{i1}')
               plt.ylabel(f'{v1}')
               plt.xticks(rotation=45,ha="right")
               plt.legend()
               self.SaveVisualize_Data()
               plt.show()
               print("Line Plot Creeate.....")
               print("Display The Line Plot...")
               print("Save image...")
               print()
             else:
                print("Invalid Column Name")  

         else:
            x = input("Enter X-axis Column Name:")
            y = input("Enter Y-axis column Name")
            if x in self.data.columns and y in self.data.columns:
               plt.plot(self.data[x],self.data[y],label=x,marker="o",color="green")
               plt.title(f"{x} by {y}")
               plt.xlabel(f'{x}')
               plt.ylabel(f'{y}')
               plt.xticks(rotation=45,ha="right")
               plt.legend()
               self.SaveVisualize_Data()
               plt.show()
               print("Line Plot Creeate.....")
               print("Display The Line Plot...")
               print("Save image...")
            else:
               print("Invalid Column Name")   
      except AttributeError:
         print()
         print("Please LoadData....")
         print()   



   def Scatter_plot(self):
      try:
         print(self.data.head(2))
         ask =input("If You Create Pivot Table (yes/no)").lower()

         if ask == "yes":

             i1 = None
             v1= None
             a1 = None
         
             i1 = input("Enter Your Index")
             v1 = input("Enter Your Values")
             a1 = input("Enter Your aggfunc like [mean,sum,count]")

             if i1 in self.data.columns and v1 in self.data.columns:
               print()
               self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1).reset_index()
               print(self.table)

               sns.scatterplot(data=self.table,x=i1,y=v1,label=v1)
               plt.title(f"{i1} by {v1}")
               plt.xlabel(f'{i1}')
               plt.ylabel(f'{v1}')
               plt.legend()
               plt.xticks(rotation=45,ha="right")
               self.SaveVisualize_Data()
               plt.show()
               print("scatter Plot Creeate.....")
               print("Display The scatter Plot...")
               print("Save image...")
               print()
             else:
                print("Invalid Column Name")  

         else:
            x = input("Enter X-axis Column Name:")
            y = input("Enter Y-axis column Name")
            if x in self.data.columns and y in self.data.columns:
               sns.scatterplot(data=self.data,x=x,y=y,label=y)
               plt.title(f"{x} by {y}")
               plt.xlabel(f'{x}')
               plt.ylabel(f'{y}')
               plt.legend()
               plt.xticks(rotation=45,ha="right")
               self.SaveVisualize_Data()
               plt.show()
               print("scatter Plot Creeate.....")
               print("Display The scatte Plot...")
               print("Save image...")
            else:
               print("Invalid Column Name")   
      except AttributeError:
         print()
         print("Please LoadData....")
         print()   

   
   def pie_plot(self):
      try:
         print(self.data.head(2))
         i1 = None
         v1= None
         a1 = None

         i1 = input("Enter Your Index")
         v1 = input("Enter Your Values")
         a1 = input("Enter Your aggfunc like [mean,sum,count]")

         if i1 in self.data.columns and v1 in self.data.columns:
            print()
            self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1).reset_index()
            print(self.table)

            plt.pie(self.table[v1], labels=self.table[i1], autopct="%1.1f%%")
            plt.title(f"{i1} by {v1}")
            plt.legend()
            self.SaveVisualize_Data()
            plt.show()
            print("pie Plot Creeate.....")
            print("Display The pie Plot...")
            print("Save image...")
            print()
         else:
            print("Invalid Column Name")  
   
      except AttributeError:
         print()
         print("Please LoadData....")
         print()   

  
   def Hist_plot(self):
      try:
         print(self.data.head(2))
         
         col = input("Enter X-axis Column Name:")

         if col in self.data.columns:
            plt.hist(self.data[col],bins=10)
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.title(f"{col} Histogram")
            plt.xticks(rotation=45,ha="right")
            self.SaveVisualize_Data()
            plt.show()
            print("Histogram Plot Creeate.....")
            print("Display The Histogram Plot...")
            print("Save image...")
            print()
         else:
            print("Invalid Cloumn Name")   

      except AttributeError:
         print()
         print("Please LoadData....")
         print()  


   def stack_plot(self):
        print(self.data.head(2))  
        
        w = input("Enter Column Name")
        x = input("Enter  Column Name:")
        y = input("Enter  column Name")
        
        table = self.data.groupby(w)[[x,y]].sum().reset_index().sort_values(by=w)

        plt.stackplot(table[w].astype(str),table[x],table[y],labels=[x,y],alpha=0.8)
        plt.xlabel(w)
        plt.ylabel(" Total Value")
        plt.title(f" {w} Stack plot")
        plt.legend()
        plt.xticks(rotation=45,ha="right")
        self.SaveVisualize_Data()
        plt.show()
        print("stack Plot Creeate.....")
        print("Display The stack Plot...")
        print("Save image...")
        print()
      



   def HeatMap(self):
      try:
         print(self.data.head(2))
         
         num = self.data.corr(numeric_only=True)
         sns.heatmap(num,annot=True)
         plt.title("Correlation Of Cloumn")
         plt.xticks(rotation=45,ha="right")
         self.SaveVisualize_Data()
         plt.show()
         print(" Heatmap Creeate.....")
         print("Display The Heatmap...")
         print("Save image...")
         print()

      except AttributeError:
         print()
         print("Please LoadData....")
         print() 



   def Box_plot(self):
      try:
        print(self.data.head(2))  
        

        x = input("Enter X-axis Column Name:")
        y = input("Enter Y-axis column Name")
        hue=input("Enter Your Hue Perameter")

        hue = hue if hue.strip() in self.data.columns else None

        sns.boxplot(data=self.data,x=x,y=y,hue=hue)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{x} by {y}")
        plt.xticks(rotation=45,ha="right")
        self.SaveVisualize_Data()
        plt.show()
        print("Box Plot Creeate.....")
        print("Display The Box Plot...")
        print("Save image...")
        print()
      except AttributeError:
         print()
         print("Please LoadData....")
         print()              


   def subplots(self):
      try:
         print(self.data.head(2))
         i1 = None
         v1= None
         a1 = None
         
         i1 = input("Enter Your Index")
         v1 = input("Enter Your Values")
         a1 = input("Enter Your aggfunc like [mean,sum,count]")

         if i1 in self.data.columns and v1 in self.data.columns:
               print()
               col = input("Enter X-axis Column Name:")
               row = input("Enter Y-axis column Name")

               self.table = self.data.pivot_table(index=i1,values=v1,aggfunc=a1).reset_index()
               print(self.table)

               fig , ax= plt.subplots(1,2, figsize=(12, 5))
               ax[0].plot(self.table[i1], self.table[v1], marker='o', label=v1)
               ax[0].set_title(f"{i1} vs {v1}")
               ax[0].set_xlabel(i1)
               ax[0].set_ylabel(v1)
               ax[0].legend()

               ax[1].bar(self.data[col],self.data[row])
               ax[1].set_title(f"{col} by {row}")
               ax[1].set_xlabel(f'{col}')
               ax[1].set_ylabel(f'{row}')
 

               plt.xticks(rotation=45,ha="right")
               plt.tight_layout()
               self.SaveVisualize_Data()
               plt.show()
               

         else:
            print("invalid Column Name..")

      except AttributeError:
         print()
         print("Please LoadData....")
         print() 

      

   def Visualize_Data(self):
      while True:
         print("===Data Visualization===")
         print("1.Bar Plot")
         print("2. Line Plot")
         print("3. Scatter Plot")
         print("4. Pie Chart")
         print("5. Histogram")
         print("6. Stack Plot")
         print("7. HeatMap")
         print("8. Boxplot")
         print("9. Subplots")
         print("10.Conclusion")
         print("11. Exit")

         try:
            ch = int(input("Enter Your Choice"))

            match ch :
               case 1:
                  print("===Bar Plot===")
                  self.bar_plot()
               case 2:
                  print("===Line Plot===")
                  self.Line_plot()
               case 3:
                  print("===Scatter Plot===")
                  self.Scatter_plot()
               case 4:
                  print("===Pie Chart===")
                  self.pie_plot()
               case 5:
                  print("===Histogram===")
                  self.Hist_plot()
               case 6:
                  print("===Stack Plot===")
                  self.stack_plot()
               case 7:
                  print("===HeatMap===")
                  self.HeatMap()
               case 8:
                  print("===BoxPlot===")
                  self.Box_plot()      
               case 9:
                  print("===Subplot===")
                  self.subplots()
               case 10: 
                  print("===Conclusion===")
                  print()
                  print()

                  print("Total Record",self.data.shape)
                  print()
                  print("Total Column",self.data.columns)
                  print()

                  if "Sales" in self.data.columns and "Region" in self.data.columns  and "Profit" in self.data.columns and "Category" in self.data.columns:
                     max = self.data["Sales"].idxmax()
                     print("Highest Sales",self.data.loc[max,"Sales"])  
                     print()
                 
                     m = self.data["Profit"].idxmax()
                     print("Highest Profit",self.data.loc[m,"Profit"]) 
                     print() 
                   
                  
                  
                     print("Highest Region by Sales",self.data.groupby("Region")["Sales"].sum().sort_values(ascending=False).head(1))
                     print()
                     print("Highest Region In Profit  ",self.data.groupby("Region")["Profit"].sum().sort_values(ascending=False).head(1))
                     print()
                     
                     print("Highest Category by Sales",self.data.groupby("Category")["Sales"].sum().sort_values(ascending=False).head(1))
                     print()
                     print("Highest Category In Profit  ",self.data.groupby("Category")["Profit"].sum().sort_values(ascending=False).head(1))
                  else:
                     print("Not Fount Column Name") 


               case 11:
                  break
               case _:
                  print()
                  print("Invalid Input....")
                  print()      

         except ValueError:
            print()
            print("Invalid Input...")
            print()      

                
            
s = Visualiztion()
if __name__ == "__main__":
      while True:
         print("===============Data Analysis & Visualization Program===============")
         print("Please Select An Option:")
         print("1. Load Dataset")
         print("2. Explore Data")
         print("3. Handle Missing Data")
         print("4. Perform DataFrame Operations")
         print("5. Generate Descriptive Statistics")
         print("6. Data Visualization")
         print("7. Exit")
         print("===================================================================")
         print()
         try:
            ch = int(input("Enter Your Choice"))
            print()
            match ch :
               case 1:
                  print("===Load Dataset===")

                  path = input("Enter Your Path Of The Dataset (CSV File)  :")
                  s.Load_Data(path)
                  print("Data Loaded Successfully!")
                  print()
                  
               case 2:
                  print("===Explore Data===")

                  print()
                  s.Explore_Data()

               case 3:
                  print("===Handle Missing Data===")

                  print()
                  s.Clean_Data()

               case 4:
                  s.Mathematical_Operations()
                  
               case 5:
                   s.Generate_Descriptive_Statistics()
               case 6:
                  
                  s.Visualize_Data()
               
               case 7:
                  print("Exiting The Program. GoodBye...!")
                  exit()
               case _:
                  print()
                  print("...Invalid Input....")
                  print()
               
         except ValueError:
            print()
            print("Invalid Input...")
            print()