# CourseDems

## Inspiration
Psychology says we are more social with people who are similar to us in our backgrounds, ethnically, gender-based, or financially and that we tend to improve our social, emotional, and academic intelligence in more diverse environments. CourseDems allows students to search up the diversity of courses at their universities.

## What it does
CourseDems is very user friendly, with only 2 inputs. First, the user finds their college of choice, and then selects the choices of courses where data is available. The backend of the code will go through the data gathered, and then produce 2 graphs, one on the gender demographics of the respective class, and one on the racial demographics. 

## How we built it
To gather the data, we created a Google Form and shared it with multiple universities in our area: UNC Chapel Hill, NC State, Duke University, and UNC Charlotte. If the data was distributed and somewhat accurate to our liking, we entered the data into our csv. Then to organize the data we stored them into nested dictionaries and list. The user interface was built with the Streamlit API, and the graphs were built with plotly from the stored data.

## Challenges we ran into
 We faced many challenges during our project. First, getting our survey out and trying to rely on reliable feedback was difficult since there wasn't originally enough data from the schools. 
Second, after getting the data, we struggled with how to organize it and read it from the csv, as we kept running into type errors due to not being able to iterate through the dictionaries at first, so we had to create many temporary variables to help us achieve reading the csv. 
Later, when displaying the graphs, we originally tried to generate graphs with matplotlib and pyplot, but realized that pyplot was no longer compatible with Streamlit so we had to switch to plotly and the graphs didn't originally display on the web page. So we had to keep tinkering around with the graph's functions and rearrange how the data is read with the plotly express.

## Accomplishments that we're proud of
We are very proud that we were able to create a good foundation for this app to help display the diversity of classes at the university level and build it on a nice and easy to use user interface.

## What we learned
We learned how to collaborate in a short time frame, and iterate and read through csv files. We also had the opportunity to better learn the pandas, plotly, and streamlit API.

## What's next for CourseDems
 We hope to gather more diversity information on more courses within the universities we have listed and begin to add more universities in the near future. It would also be nice to add more features with the Rate My Professor API and attaching GradeToday ratings and distributions later on for the available courses.
