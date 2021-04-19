#string concatination using f string.
print("Pick one of the 2 inputs. Add your own inputs wherever necessary")
name=input("Name: ",)
sex=input("Are you male or female: ",)
age=input("Teenager or adult: ",)
subject=input("Name any subject: ",)
feeling=input("Do you love or hate the subject? ",)
adj=input("Give and adjective for the subject chosen: ",)

madlib = f"Hey! My name is {name}. I am a {sex}. I fall under the age group of {age}.\
My favourite subject is {subject}. I {feeling} it because it so super duper {adj}!!!"

print(madlib)


