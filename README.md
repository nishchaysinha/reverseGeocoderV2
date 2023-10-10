### Reason for this project:

I wanted to see how far i’ve come as a developer, hence I am going to put everything i’ve learnt in the past year into this project.

I recently reviewed my old work and this was one of the projects that was one of my most disappointing and shabby repos. All the unhealthy habits have been practiced during this project. I want my work to reflect perfection and consistency rather than a throw a prototype together kind of vibe.

I hope i do this project justice and make something respectable out of it.

## Description

so a reverse geocoder gives a locations address when its given the locations latitude and longitude as parameters. So essentially this is a way to make reverse geocoders free.

# Flaws with old version

1. Very slow response time(1 second is unacceptable)
2. Terrible code structure(It seems like a fifth grader wrote it)
3. not nearly as optimized as it could’ve been
    1. the entire driver closes after every function which is not feasible
4. No proper documentation or timeline or version control as a matter of fact
5. frequent crashes so it was pretty much very unreliable

# V2-0.0.0; 31/05/2023

- Proposed Folder/Project Structure (finalized)
    - Folder
        - 📝main.py
        - 🔐config.json
        - 📄Dockerfile
        - 📂config
            - 📝configure.py
        - 📂core
            - 📝reversegeocoder.py
            - **Future Expansion**
        - 📂utils
            - 📝csvwriter.py
            - 📝csvreader.py
            
- Ideation on what to improve
- Plan to Rectify flaws in v1

[V1 Source Code](https://github.com/nishchaysinha/GMAPs-reversegeocoder)
