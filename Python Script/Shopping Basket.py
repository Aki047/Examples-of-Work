#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#step 0 - Prompt user to input search or start an order or end
#If starting an order:
    #step 1 - Generate Order Number
    #step 2 - Prompt user to input customer id, Product_number, Item, qty, price
    #step 3 - Create a dictionary for each product entry
        #step 4 - Ask user for more product details  if not go to step 6
        #step 5 - If more products, create separate dictionaries
    #step 6 - Compile product dictionaries into shopping basket dictionary
    #step 7 - convert shopping basket dictionary to json file with order no in file name
#End Step - Return user to step 0


# In[54]:


import json  


# In[55]:


#step0
order_no = 100   

scanner = (input("Enter an option  (Start Order / Search Order / End): "))

while scanner != 'End':
    
    while scanner == 'Start Order':
        #step 1 - Generate Order Number

        order_no += 1
        print("Order Number: ", order_no)

        shopping_basket = {}

        #step 2 - Prompt user to input customer_iD, product_number, item, qty, price
        customer_id = int(input("Enter Customer ID: "))

        product_entry = 'Yes'
        entry_no = 0

        while product_entry == 'Yes':
            entry_no += 1
            product_number = int(input("Enter Product Number: "))
            item = input("Enter Item Name: ")
            qty = int(input("Enter Item Quanity: "))
            price = float(input("Enter Item Price: "))

            #step 7 - convert shopping basket dictionary to json file with order no in file name
            product = {"order_no": order_no, "customer_id": customer_id,
                            "product_number": product_number, "item": item,
                            "qty": qty, "price": price}

            product_key = 'product_'+str(entry_no)

            shopping_basket[product_key] = product
            product_entry = (input("Add Product Details (Yes / No): "))

        File_Name = 'order_'+ str(order_no)+".json"

        with open(File_Name, "w") as fp:
            json.dump(shopping_basket, fp)

        print("Thank you for shopping with us!")
        print("Below are the order details")
        print(shopping_basket)

        scanner = (input("Enter an option  (Add another Order? / End): "))

    while scanner == 'Search Order':        
        print ("Input Order Number")
        filename = str(input())
        
        try:
            with open('Order_' + filename + '.json', 'r') as f:
                data = json.load(f)
                print (data) 
        except:
            print('Invalid Order No')
            
        scanner = (input("Enter an option  (Start Order / Search Order / End): "))

print("Have A nice Day!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




