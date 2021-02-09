import pandas as pd
from pyspark.sql import SQLContext
from pyspark.sql.functions import when
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType, DecimalType,DoubleType
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("PysparkSql").getOrCreate()

#Reading csv files
u = spark.read.csv("Mall_Customers.csv",header =True,inferSchema='True')
v = spark.read.csv("employee.csv",header =True)

print("\nThere are 2 tables.\nOne is containing spending rate of a customer\nOther contains job details of the customer ")
print("Select the operation you want to perform\nPress 1 to view data\nPress 2 to insert data\nPress 3 to delete data\nPress 4 to perform joins\n")

key = int(input())
if (key<5 and key>0):
	while(key<5 and key>0):
		if(key==1):
			print("Mall customer table")
			u.show()
			print("Employee table")
			v.show()
		elif(key==2):
			print("Press 1 to insert into Mall customers table\nPress 2 to insert into Employee table")		
			choice = int(input())
			
			if(choice<=2 and choice>0):
				if(choice==1):
					n = []
					new = []
					new.append(int(input("Enter Customer id  ")))
					new.append(input("Enter Gender  "))
					new.append(int(input("Enter Age  ")))
					new.append(int(input("Enter Annual Income in k$  ")))
					new.append(int(input("Enter Spending score in range(1-100)  ")))
					n.append(new)
					new_df = spark.createDataFrame(n)
					u = u.union(new_df)
					u.write.format("csv").mode("overwrite").save("Mall Customers.csv",header=True)
					print("\nVALUES INSERTED SUCCESSFULLY\n")
					u.show()
					
				else:
					n = []
					new = []
					new.append(int(input("Enter Customer id  ")))
					new.append(input("Enter Profession  "))
					n.append(new)
					new_df = spark.createDataFrame(n)
					v = v.union(new_df)
					v.write.format("csv").mode("overwrite").save("Employee.csv",header=True)
					print("\nVALUES INSERTED SUCCESSFULLY\n")
					v.show()
					
			else:
				print("\nINCORRECT OPTION")
		elif(key==3):
			print("Press 1 to delete from Mall customers table\nPress 2 to delete from Employee table")		
			choice = int(input())
			
			if(choice<=2 and choice>0):
				if(choice==1):
					n = int(input("Enter Customer id  "))
					y = u.filter(u.CustomerID==n)
					u = u.subtract(y)
					u.write.format("csv").mode("overwrite").save("Mall Customers.csv",header=True)
					print("\nVALUES DELETED SUCCESSFULLY\n")
					u.show()
					
				else:
					n = int(input("Enter Customer id  "))
					y = v.filter(v.CustomerID==n)
					v = v.subtract(y)
					v.write.format("csv").mode("overwrite").save("Employee.csv",header=True)
					print("\nVALUES DELETED SUCCESSFULLY\n")
					v.show()
			else:
				print("\nINCORRECT OPTION")
		else:
			print("FULL OUTER JOIN")
			y = u.join(v,u.CustomerID ==  v.CustomerID,"fullouter").show()
			print("LEFT JOIN")
			y = u.join(v,u.CustomerID ==  v.CustomerID,"left").show()
			print("RIGHT JOIN")
			y = u.join(v,u.CustomerID ==  v.CustomerID,"right").show()
			print("INNER JOIN")
			y = u.join(v,u.CustomerID ==  v.CustomerID,"inner").show()
			
		print("Select the operation you want to perform\nPress 1 to view data\nPress 2 to insert data\nPress 3 to delete data\nPress 4 to perform joins\n")
		key = int(input())
	print("\nIncorrect Option")
else:
	print("\nIncorrect Option")
	spark.stop()
