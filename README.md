# creating.django.api
### First Django API experimentation:
I created this project to experiment with CRUD operations in Django web framework. This tutorial was completed with class-based views. Function-based views will be covered in a separate repo. The steps included in this git repo were:

    1. Post method
    2. Get method
    3. Patch method
    4. Delete method

I then tested the functionality of the methods implemented above. As part of the method implementations, we also created a `CartItemSerializer` to handle querysets and model instances by turning them into native Python datatypes and then into easily readable JSON or XML (in our case JSON). `CartItemSerializer` also provides deserialization, converting parsed data back into complex types.