def generate_zero_shot_prompt(row):
    return f"""
    You are a Fake News detection AI. Based on the provided details, classify the statement into one of these categories: 
    true, mostly-true, half-true, false, barely-true, pants-on-fire.

    Statement: "{row['statement']}"  
    Speaker: {row['speaker']} ({row['speaker_job_title']})  
    Context: "{row['context']}"  
    Past Truthfulness: {row['barely_true_counts']} barely true, {row['false_counts']} false, {row['half_true_counts']} half-true, {row['mostly_true_counts']} mostly true, {row['pants_on_fire_counts']} pants-on-fire.  

    Choose only one category from: true, mostly-true, half-true, false, barely-true, pants-on-fire.  
    Answer with only the category name and nothing else.
    """
def generate_few_shot_prompt(row, formatted_examples):
    return f"""
    You are a Fake News detection AI. Based on the provided details, classify the statement into one of these categories: 
    true, mostly-true, half-true, false, barely-true, pants-on-fire.

    Learn from these training examples:
    {formatted_examples}  

    Now classify this new statement:
    Statement: "{row['statement']}"  
    Speaker: {row['speaker']} ({row['speaker_job_title']})  
    Context: "{row['context']}"  
    Past Truthfulness: {row['barely_true_counts']} barely true, {row['false_counts']} false, {row['half_true_counts']} half-true, {row['mostly_true_counts']} mostly true, {row['pants_on_fire_counts']} pants-on-fire.  

    Choose only one category from: true, mostly-true, half-true, false, barely-true, pants-on-fire.  
    Answer with only the category name and nothing else.
    """

def generate_cot_prompt(row):
    """Generate chain-of-thought prompt for LIAR dataset"""
    return f"""
You are a fake news detection AI. Your task is to classify political statements into one of the following categories:

➡️ Categories: true, mostly-true, half-true, false, barely-true, pants-on-fire

You will be shown a statement along with speaker metadata and context. For each case, use step-by-step reasoning to explain your judgment before assigning a label.

---

### 🔍 EXAMPLE 1
**Statement**: polling show nearly 74 percent national rifle association member support requiring background check gun sale  
**Speaker**: Lena Taylor (State Senator District 4)  
**Subject**: civil-rights, government-regulation, guns  
**Context**: news release  
**Label**: true  
**Reasoning**: The statement includes a specific statistic, suggesting verifiability. The speaker is a public official, and the topic is based on empirical data. The formal setting (news release) supports accuracy.

---

### 🔍 EXAMPLE 2
**Statement**: left city 43 million bank  
**Speaker**: Maurice Ferre (Former Mayor of Miami)  
**Subject**: job-accomplishments  
**Context**: interview with Newsmax  
**Label**: barely-true  
**Reasoning**: The statement is vague and lacks context. As a former mayor, the speaker has a motive to frame events favorably. The interview setting may lead to exaggeration or bias.

---

### 🔍 EXAMPLE 3
**Statement**: say couldnt take stimulus money required universal building code  
**Speaker**: Sarah Palin (no title listed)  
**Subject**: energy, federal-budget, stimulus  
**Context**: book "Going Rogue"  
**Label**: false  
**Reasoning**: The claim is overly simplified and lacks nuance. The source is a political memoir, which suggests subjectivity. The phrasing is absolute and omits key policy details.

---

### 🔍 EXAMPLE 4
**Statement**: the income tax rate was 90 percent under President Eisenhower
**Speaker**: Alexandria Ocasio-Cortez (US Representative)
**Subject**: taxes, history
**Context**: 60 Minutes interview
**Label**: mostly-true
**Reasoning**: This statement references a verifiable historical fact about tax rates, though it simplifies a complex tax structure. The highest marginal rate was indeed around 90%, but applied only to the very highest incomes. The speaker conveys the core truth while omitting nuances.

---

### 🔍 EXAMPLE 5
**Statement**: there are more trees on Earth today than there were 100 years ago
**Speaker**: Matt Ridley (Science writer)
**Subject**: environment, history
**Context**: public lecture
**Label**: half-true
**Reasoning**: This statement has elements of truth but is misleading without context. While tree count may have increased in some areas due to reforestation efforts, old-growth forests have declined significantly. The quality and biodiversity of forests matter as much as raw numbers.

---

### 🔍 EXAMPLE 6
**Statement**: covid-19 vaccines alter your DNA
**Speaker**: anonymous social media user
**Subject**: health, science
**Context**: viral Facebook post
**Label**: pants-on-fire
**Reasoning**: This claim contradicts established scientific understanding of how mRNA vaccines work. These vaccines don't enter the cell nucleus where DNA is stored, making genetic modification impossible. The claim shows either intentional deception or complete scientific ignorance and can cause serious public harm.

---

Now evaluate the following new statement:

**Statement**: "{row['statement']}"  
**Speaker**: {row['speaker']} ({row['speaker_job_title']})  
**Context**: "{row['context']}"  
**Past Truthfulness Stats**:  
- Barely true: {row['barely_true_counts']}  
- False: {row['false_counts']}  
- Half-true: {row['half_true_counts']}  
- Mostly true: {row['mostly_true_counts']}  
- Pants-on-fire: {row['pants_on_fire_counts']}  

---

### 🧠 Your Task:
1. Provide your **step-by-step reasoning** based on the speaker, context, tone, and wording of the statement.
2. Then **conclude** with **only one** of the following labels:  
   ✅ true, mostly-true, half-true, false, barely-true, pants-on-fire.
"""