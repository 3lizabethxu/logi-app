# Django CRUD Inventory Management Application

# Overview
This project uses Django and SQLite as the back-end and Bootstrap as front-end.
Django helps the security of the system. SQLite is great for lower traffic sites but will struggle if scaled.

# Products Page
(Default Landing Page)
The products page allows users to create,edit,delete and view a list of inventory items. 
The table on the products page displays information about an inventory item, some key details (price, catergory) and where the inventory item is located.
Users are able to assign inventory to specific warehouse locations when they create or edit an inventory item.

* By clicking "Create Inventory Item" users are able to fill out an inventory form that allows them to input the name,price,category and location of the item they would like to add in inventory.
* By clicking "Edit" users can edit details of an inventory item from the database
* By clicking "Delete" users can remove an inventory item from the database


# Warehouse Page
The warehouse page all allows users to create and edit warehouses.

* By clicking "Create Warehouse/Location" users are able to fill out name and location of a new warehouse to be added to the database.
* By clicking "Edit" users can edit details about a warehouse in the database.

# Next Steps
For the purpose of this project, SQLite will suffice but a more scalable back-end framework like like would be chosen if this were used for production. 
For example, PostgreSQL.
