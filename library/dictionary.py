task = {"goodreads": "Rate the sentiment of this book review. ",
         "oamm": "Does the following text show evidence of ",
         "crisp": "Does the following text show evidence of "}

format = {"goodreads": "Rate on a scale from 0 = bad to 5 = good. ",
        "oamm": "Rate on a scale from 1 = to 5 = ",
        "crisp": "Assign a 1 if there is evidence and a 0 if there is not. "}

persona = {"tree of thoughts": "Imagine there are 3 experts answering the question. All experts will write down 1 step of their thinking and share with the group and then move onto the next step. At each step eliminate any expert that is wrong. ",
           "therapist persona": "You are a therapist. ",
           "psychologist persona": "You are a pyschologist. "}

logic = {"no": "Do not explain your logic, only provide a numeric rating. ",
         "chain": "Think carefully and logically. ",
         "steps": "Think this through step by step. "} # yes = chain of thought

construct = ["meaning making", "negative core beliefs", "emotional invalidation", "perspective taking"]

model_name = {"meta-llama/Llama-3.3-70B-Instruct": "llama3.3",
               "meta-llama/Llama-3.2-1B-Instruct": "llama3.2_1b", 
               "meta-llama/Llama-3.2-3B-Instruct": "llama3.2",
               "meta-llama/Llama-3.1-8B": "llama3.1",
               "llama3.3": "llama3.3",
               "llama3.2": "llama3.2",
               "llama3.2_1b": "llama3.2_1b",
               "llama3.1": "llama3.1"}