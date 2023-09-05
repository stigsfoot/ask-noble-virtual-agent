# **Mitigating AI Bias, with …Bias**


![alt_text](images/image1.jpg "image_tooltip")
Unrelated photo taken by Author

_This article is part of my Data Trust series of talks and writing. The purpose of these articles are to break down complex but important socio-technical topics in a manner that is accessible to both practitioners and non-practitioners._


#### **Updated: 12/2022 to include a video of one of my speaking engagements covering this post at Strangeloop Conf, STL-fall 2022.**


### **With great power comes complexities**

Most tools we use today leverage AI/ML from the moment we wake up and while we sleep.

Humans build Machine Learning, and humans are inherently biased.

Since humans aren’t perfect, we encode our biases into the data we use to train AI.

Encoding our biases in machine learning training often results in unfair treatment or harm against protected classes, groups, and individuals.

**We’ll cover how to get around this, but there is one catch. **You cannot guarantee fairness for your AI application, and this is because there is no single definition of fairness. How you define fairness for one solution will be different for another.

Issa Rae Reaction

Human-centered machine learning practitioners leverage fairness metrics and bias mitigation algorithms to solve this catch. Essentially countering bias, we don’t want with good bias using these methods.

_A lot has been written about fairness, statistical, and algorithmic bias in the last few years, so while I may not dive deep into all the nuances, know that eliminating discrimination in your AI is hard work. I have shared more resources at the end of this post._


![alt_text](images/image2.png "image_tooltip")
(Moritz Hardt, 2017)


### **We’re only human, and we encode our bias into AI.**


![alt_text](images/image3.jpg "image_tooltip")
Photo taken by Author


#### **Storytime**

_I’m sharing my lived experience from an incident 18 years ago in Richmond, Virginia, to make a larger point on the complexities of mitigating bias so that you can reduce risk._

It’s 2004; Done with work, I changed into my sweats and white t-shirt, stuffed work clothes into my gym bag, and started the 15-minute walk from my office to the gym.

I went to cross a one-lane road but hopped back onto the sidewalk as two police vehicles, one driving in the opposite direction of traffic, blocked my path.

Officers hopped out, yelling what many black males have heard in many US cities.


    “Get down on the ground now!”

Between the time it took to take off my headphones, I was on the pavement, face to the ground, as my arms stretched painfully behind me while I got detained.

It was a case of mistaken identity, and I fit the description of an apparent criminal.

They let me go. I was traumatized, so I turned around and went home.

When thinking about your AI team, look for a diverse and representative group because your final solution will be better for it.


#### **Do members of your AI team have similar lived experiences?**

…and do they have a voice?

As a digital product delivery practitioner, my experience influences how I lead teams to ship software, including[ AI](https://www.chatbotconference.com/). Your team should prioritize bringing together a diverse and representative group of people in your organization across functions.

Empowered diverse and representative AI teams bring objective perspectives with metrics to show how software can cause harm in addition to success measures or quantifiable objectives to deliver safe, secure, private, performant, and usable software.


### **Bias Mitigation Strategies for AI/ML, aka adding good bias**


![alt_text](images/image4.png "image_tooltip")
**Adapted from:** Mehrabi et al. Survey on Bias & Fairness in ML[ Cornell University ARXIV research](http://arxiv.org/pdf/1908.09635.pdf) 2022

Let’s walk through a thought experiment with how vision-based AI could assist a law enforcement officer without bias in a high-stakes scenario like this.

Assuming you determined an AI is best to solve the problem, define the need, and you need to map those needs to features. We could look at race, gender, perhaps my age, the clothes I had on, etc.

**Fortunately (and thankfully), race, gender, and age are protected classes in United States labor laws, so that’s a “no-go.”**

So what do we do…ok let’s look to an AI to use my clothing to help an officer decide to detain or leave me be.

_It is worth saying that this is just an example. In a real-world scenario, clothing alone would be a terrible correlation to identifying a potential criminal._


### **Strategize — Principles and metrics:**

Collect a diverse and representative group of people in your organization across functions to determine if this is a problem an[ AI](https://www.chatbotconference.com/) is best suited to solve.

Work together to agree on values and fairness objectives and indicators as metrics to address with your team and customers based on your values.

As part of the Strategize phase, you codify one of many definitions of fairness with these baseline metrics.

Amongst other signals, we’re looking at clothing for our thought experiment. We may look at a few** examples of fairness metrics. **Metrics like:



* **Disparate impact** — “Compares the proportion of individuals that receive a positive output for two groups: an unprivileged group and a privileged group.” See also[ IBM Disparate Impact Remover](https://www.ibm.com/docs/SSQNUZ_3.5.0/wsj/model/wos-fairness-ovr.html).
* **Demographic parity **— satisfied if our model’s classification results are not dependent on a given sensitive attribute. See also some[ practical approaches from Google Research](https://research.google.com/bigpicture/attacking-discrimination-in-ml/).
* **Equalized odds **— according to Google Research, “checks if, for any particular label and attribute, a classifier predicts that label equally well for all values of that attribute.”

There are more. AIF360 has quite a few of these if you want to dig in[ https://aif360.readthedocs.io/](https://aif360.readthedocs.io/)


### **Synthesize — Ask the right questions:**


#### **The classic question of how do you verify a sufficient sample size and quality of data for training?**

Be sure to watch out for secondary effects. These are unexpected drawbacks or perverse or opposite results that lead to unintended consequences.

More than removing protected classes from your training data in the example above may be required. Consider what if we are wrong in how weighting the shoes someone is wearing. Or what if this[ AI-drive](https://www.chatbotconference.com/) solution is used maliciously to filter out people dressed a certain way?


#### **How do we teach a machine to consider the historical trauma, discrimination, and opportunity denial black and brown people have endured due to historical and societal issues?**

I recently shared a panel with Dr. Nicol Turner Lee of the Brookings Institute. She mentioned something that stuck with me, that socio-technical harm is also experienced through ‘**Traumatized data**’. Trauma is the collective psychological, emotional, and cognitive distress experienced by African Americans historically, such as my perception of bias from my incident eighteen years ago.


#### **If you haven’t already, check out the article, Dr. Turner Lee is also a fantastic human, so give her a follow.**

So back to the story. Was I unjustly harmed? Yes. Physically then and psychologically now.

Eighteen years later, I still think about where this incident could have ended me. I’m traumatized by this incident.

The key takeaway from this and the next section is to understand the payoffs of being right vs. being wrong so that you can fight bad bias with mitigation and good interpretable bias.


### **Analyze then train — Lead with your fairness indicators**


#### **Weave your AI bias mitigation approach throughout your data science lifecycle.**

**Data Collection. **The dataset was sourced and inspected for sample diversity. Look into concepts like data-centric AI, and principle-centric AI. I have found resources like Google Research PAIR approach to Data Collection and Evaluation helpful, and I think you will too.

**Pre-processing**. If you can modify the training data and have fairness metrics for your datasets, then run tests on raw data to detect bias and use pre-processing algorithms to mitigate risk. A pre-processing algorithm, such as a re-weighing algorithm where you change the weights applied to your training samples, can be used.

**During training or in-processing.** If you can modify the learning algorithm, then an in-processing algorithm such as adversarial debiasing can be used to mitigate bias.

**Post-processing and classifier metrics.** AI Bias mitigation can be applied to predicted labels by tuning your labels to address harms in underprivileged and protected classes. However, you may sometimes find that you can’t modify the training data or the learning algorithm. In this case, a post-processing algorithm can be used.

**Reprocess and or retrain.**

You should ensure you run unit tests for accuracy and discrimination along the way, then deploy.

**Interpreting machine learning models and Explaining machine learning predictions**

Doing all of this work and not being able to explain the impacts of a feature on a model’s prediction to your various stakeholders isn’t entirely useful.

NIST has a good “explainer” of Explainable AI (XAI). XAI is a field of ML interpretability techniques whose aims are to understand machine learning model predictions and explain them in human and understandable terms to build trust with stakeholders, both internal teams and the user.

Interpretability, on the other hand, focuses on model understanding techniques. In contrast, explainability more broadly focuses on model explanations and the interface for translating these explanations in human-understandable terms for different stakeholders.

I will cover XAI and related topics from the angle of Data, Feature, and Model Trust in future blog posts and speaking engagements. Stay tuned.


### **Improve — Build AI value that avoids harm.**

Keeping a human in the loop with external interventions on your raw data is the final lesson.

At this point, you have your definition of fairness and related metrics, you have your bias mitigation algorithms woven into your ML lifecycle, and you have your software using your model out in the wild.

Continuous capture of user feedback is essential here. There are a few patterns that I can share from a human-centered ML standpoint, but I’ll use my 3C (Context, Choice, Control) framework:


    If you are calibrating for trust with your solution, you must also provide enough context for how their data or feedback will be used to better the experience, and provide them the ability to opt out.

Context, Choice, Control

When there is no human in the loop (a diverse set of stakeholders) to review, refine, build, deploy, evaluate, and monitor unintentional or secondary effects, it leads to these recurring incidents.

My thought experiment fell apart quickly because eliminating **bad bias** is hard work. By understanding where the bias is, we can introduce **good bias** through these strategies and approaches.


---


### **Additional reading:**



* Data Trust, Stewardship & Privacy https://medium.com/@nobleackerson/whats-next-for-data-privacy-and-stewardship-9c1aee17b83a
* A curated list of resources on AI Fairness & Bias https://github.com/datamllab/awesome-fairness-in-ai
* PyMetrics — Open-sources bias detection and auditing algorithms.
* Ethics Checklist (https://deon.drivendata.org) can be appended to a Jupyter notebook
* AI Explorables https://pair.withgoogle.com/explorables/
* IBM AI fairness 360 https://aif360.mybluemix.net/
* Stanford HAI https://hai.stanford.edu/taxonomy/term/59
* Microsoft Fairlearn https://www.microsoft.com/en-us/research/publication/fairlearn-a-toolkit-for-assessing-and-improving-fairness-in-ai/

**_To hear more on these topics and if you can make it out, join me in-person or remotely by registering for Refactr Tech in Atlanta and at the Strangeloop Conference in St. Louis this fall._**

_Noble currently leads the product and AI practice at Ventera Corporation in Virginia, US._

**[Join Medium with my referral link - Noble Ackerson](https://medium.com/@nobleackerson/membership)**

_[As a Medium member, a portion of your membership fee goes to writers you read, and you get full access to every story…medium.com](https://medium.com/@nobleackerson/membership)_

_Reach me on[ Twitter](https://www.twitter.com/nobleackerson)_,_ connect with me on[ LinkedIn](https://linkedin.com/in/noblea)_
