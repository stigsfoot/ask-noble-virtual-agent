# 
    **GPT Is an Unreliable Information Store**


## 
    Understanding the limitations and dangers of large language models


    
![alt_text](images/image1.jpg "image_tooltip")



    “Searching for meaning” Photo by author

Large language models (or generative pre-trained transformers, GPT) need more reliable information accuracy checks to be considered for Search.

These models are great at creative applications such as storytelling, art, or music and creating privacy-preserving synthetic data for applications. \
These models fail, however, at consistent factual accuracy due to [AI hallucinations](https://www.wired.com/story/ai-has-a-hallucination-problem-thats-proving-tough-to-fix/) and transfer learning limitations in ChatGPT, Bing Chat, and Google Bard.

First, let’s define what AI hallucinations are. There are instances where a large language model creates information that is not based on factual evidence but may be influenced by its transformer architecture’s bias or erroneous decoding. In other words, the model makes up facts, which can be problematic in domains where factual accuracy is critical.

Ignoring consistent factual accuracy is dangerous in a world where accurate and reliable information is paramount in battling misinformation and disinformation.

Search companies should reconsider “re-inventing search” by mixing Search with unfiltered GPT-powered chat modalities to avoid potential harm to public health, political stability, or social cohesion.

This article extends this assertion with an example of how ChatGPT is convinced that I have been dead for four years and how my obituary, which seems very real, highlights the risks of using GPTs for search-based information retrieval. You can try it by plugging my name into ChatGPT and then convince it that I’m alive.


    A few weeks ago, I decided to dive into some light research after learning that Google wiped $100 billion off its market cap because of a rushed demo where Bard, the ChatGPT competitor, shared some inaccurate information. The market seems to [react negatively to the reliability and trustworthiness of this tech](https://www.cnbc.com/video/2023/02/16/the-new-york-times-kevin-roose-on-his-conversation-with-microsofts-ai-powered-chatbot-bing.html), but I don’t feel we’re connecting these concerns with the medium enough.


    I decided to “egosurf” on ChatGPT. Note: I just discovered the word egosurf. We’ve all Googled ourselves before but this time with ChatGPT. \
This decision was intentional because what better way to test for factual accuracy than to ask it about me? And this decision didn’t disappoint; I consistently got the same result: **I learned I was dead.**


    
![alt_text](images/image2.png "image_tooltip")



    ChatGPT claims I died in 2019

[Here is a truncated copy](https://gist.github.com/stigsfoot/acf985bf3a22c5c46ed787e34f638991) of the entire conversation.


## 
    **ChatGPT thinks I’m dead!?**

ChatGPT insisted I was dead, doubled down when I pushed back and created a whole new persona. I now understand why large language models are unreliable information stores and why Microsoft Bing should pull the chat modality out from it’s search experience.

Oh… and I also learned had I had created other tech ventures after [my previous startup, LynxFit](https://9to5google.com/2014/12/08/google-glass-app-lynxfit-join-apx-labs/). It seems confused by what my co-founders and I built at LynxFit, and it makes up a whole story that I founded a transportation company in Ghana. Ghana? That’s also where I’m from. Wait…falsehoods mixed with truth is classic misinformation. What’s going on?

Ok, it got one fact half right and made up pretty much every other fact is upsetting. I’m pretty sure I’m still alive. At Lynxfit, I built AR software to track and coach users' workouts with Wearables, not a smart jump rope. Also, I’m Ghanaian by heritage, but I have never built a transportation app for Ghana.

All seems plausible, but ole’ Mendacious Menendez over here made up the entire thing.

OpenAI’s documentation clearly states that ChatGPT has techniques to admit its mistakes through users' contextual clues or feedback. So naturally, I gave it a few contextual clues and feedback to let it know it was “dreaming of a variant Earth-Two Noble Ackerson” and not the one from this reality. That did not work, and it doubled down and chose to fail harder.


![alt_text](images/image3.png "image_tooltip")


ChatGPT doubles down on incorrect facts. Verifying if it thinks its response is factual.

Um…are you sure? Trying to nudge a chatbot towards being factual is like yelling at a PA system that is playing back a recorded message. It is a whacky thing to do but for “research” I spent an hour with this thing. After all, [OpenAI claims it admits mistakes with some ‘prompt coaxing’](https://openai.com/blog/chatgpt/).

A total waste of time.


![alt_text](images/image4.png "image_tooltip")


Acknowledges and attempts to provide information on how it gets its evidence

A while later, it switches to a new mode after I constrain it by asking it to admit it didn’t know an answer.


![alt_text](images/image5.png "image_tooltip")


The AI insists it’s right …so I guess I’m from New Jersey

Large Language models are unreliable information stores. What can we do about this?

By design, these systems do not know what they do or don’t know.

In my grim example, I’m dead, and from New Jersey, well, I’m not. It is hard to know precisely why ChatGPT thinks this, and complex to understand why. It is possible I could be roped into a large category of tech CEOs during my startup days that built a fitness startup, one of whom passed away during that time. It conflated relationships between subjects and predicates to be convinced I had died.

GPT is trained on massive amounts of text data without any inherent ability to verify the accuracy or truthfulness of the information presented in that data.

Relying too much on large language models within Search applications, such as Bing, or as a replacement for Search, such as OpenAI’s ChatGPT, will result in adverse and unintended harm.

Put more plainly, in its current state, ChatGPT should not be considered an evolution of Search.

So should we build on top of factually unreliable GPTs?

Yes. Though when we do, we must ensure we add the appropriate trust and safety checks and the practical constraints through techniques I’ll share below. When building atop these foundational models, we can minimize inaccuracy using proper guardrails with techniques like prompt engineering and context injection.

Or, if we have our own larger datasets, more advanced approaches such as Transfer learning, fine-tuning, and reinforcement learning are areas to consider.

Transfer learning (Fine-tuning specifically) is one technique to improve the accuracy of models in specific domains, but it still falls short.

Let’s talk about transfer learning or fine-tuning, a technique replicating large language models. While these techniques can improve the model’s accuracy in specific domains, they do not necessarily solve the issue of AI hallucinations. This means that even if the model gets some things right based on the new data domain, it’s being transformed with, it may still create inaccurate or false information based on how large language models are architected.

Large language models lack deductive reasoning or a cognitive architecture which makes them epistemologically blind to what it knows it knows and its known unknowns. After all, Generative Pre-trained Transformers (aka large language models) are [incredibly sophisticated text prediction engines](https://writings.stephenwolfram.com/2023/01/wolframalpha-as-the-way-to-bring-computational-knowledge-superpowers-to-chatgpt/) and have no way to identify the patterns that lead to the facts or hallucinations they generate.

Microsoft’s ambition to integrate a fined tuned GPT within Bing is problematic and is an awful strategy when deep fakes, conspiracies, and disinformation are the norm in 2023. Today, end users require facts with sources and attribution to avoid chaos. Microsoft should know better.

Then there’s Google. I understand why Google keeps LaMDA’s large language model under wraps and only uses this emergent technology internally for Search and other services. Unfortunately, they saw Bing Chat then they panicked. Google invented most of this tech; they know the dangers. Google should know better.

For Large Language models to be a component of Search, we need ways to understand the provenance and lineage of the generated responses of these large language models.

This way, we can:



* Provide attribution of sources,
* Provide a level of confidence for each response the AI generates, or

Right now, we’re not there yet though I hope we see these innovations soon.

As part of this research, I demonstrate ways to increase factual accuracy and ward off hallucinations using the [OpenAI Text Completions model endpoint](https://platform.openai.com/docs/guides/completion/prompt-design).


![alt_text](images/image6.png "image_tooltip")


Checking factual accuracy with the GPT3 Completions Model Endpoint

In a similar example, I asked the GPT3 model, “who won the 100-meter dash at the 2020 Olympics?” \
It responds, “The 100-meter dash at the 2020 Olympics was won by Jamaica’s Shelly-Ann Fraser-Pryce.”


![alt_text](images/image7.png "image_tooltip")


An example to highlight factual accuracy (i.e., hallucinations or confabulation). Prompt: “who won the 100-meter dash 2020 Olympics?”

Sounds factual, but the truth is more nuanced as the 2020 Olympics were postponed a year due to the pandemic. For developers of large language models, it is important to take steps to reduce the likelihood of AI hallucinations. For end-users, it’s essential to bring critical thinking and not be overly reliant on AI results.

So, as a developer, what are some ways to reduce the likelihood of AI making up facts, given the flaws of large language models? One lower-barrier-to-entry approach is prompt engineering. Prompt engineering involves crafting prompts and adding prompt constraints to guide the model toward accurate responses.

Prompt engineering


![alt_text](images/image8.png "image_tooltip")


[Prompt engineering tip](https://platform.openai.com/docs/guides/completion/prompt-design) using prompt constraints to show the API how to admit it doesn’t know a fact.

Or you can feed it specific context to the domain you care about using Context injection.


![alt_text](images/image9.png "image_tooltip")


Controlling hallucination by constraining the model domain-specific prompts. “How many times have the Eagles beaten the Patriots in a Superbowl” Model responds correctly with Once.

The context ingestion method is faster and cheaper but requires domain knowledge and expertise to be effective. This approach can be particularly useful in domains where the accuracy and relevance of the generated text are critical. You should expect to see this approach in enterprise contexts such as in customer service or medical diagnosis.

Another approach is to use embedding (for example, for vector or semantic Search), which involves using the OpenAI Embeddings model endpoint to search for related concepts and terms known to be true. This method is more expensive but is also more reliable and accurate.


![alt_text](images/image10.png "image_tooltip")


Human-readable text and vectorized text pair.

AI hallucinations are a real and potentially dangerous issue in large language models. Fine-tuning does not necessarily solve the problem; however, the Embeddings approach is where a user's query is matched with the nearest, most likely factual hit in a vector database using [cosine similarity](https://github.com/openai/openai-python/blob/ede0882939656ce4289cb4f61142e7658bb2dec7/openai/embeddings_utils.py) or equivalent.


![alt_text](images/image11.png "image_tooltip")


AI confabulates additional incorrect facts about me. None of this is true.

In summary: Keeping up with the pace of innovation without breaking things.

Let’s learn from the past. To ensure factual accuracy, it’s essential to be aware of the impacts of unintentionally pushing false information given the scale OpenAI is innovating. Developers should reduce the likelihood of disproportionate product failure where incorrect information is presented in the context of factually correct information, as the hundred million plus early adopters of ChatGPT, such as through prompt engineering or vector search. By doing so, we can help ensure that the information provided by large language models is accurate and reliable.

I admire the OpenAI’s strategy of putting these tools in people's hands to get early feedback in a controlled process across industries or domains but to a point.

[Not at their scale](https://www.wsj.com/articles/microsoft-says-it-plans-multibillion-dollar-investment-in-openai-11674483180).

I do not admire the “moving fast” even if the solution is still a “somewhat broken” attitude.

Hard disagree.

Don't “move fast and break things” at this scale.

This ethos should be nuked from orbit, especially with non-deterministic transformative technology controlled by a massive startup like OpenAI. Sam Altman should know better.

For the startups innovating in this space out there. There are a lot of you; hear me out. \
The stakes are too high when misinformation leads to representational harm, [leading to hefty fines](https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions-facebook); you don’t want that loss of trust in your customers or, worse, for your startup to die.

Stakes may be low for a massive corporation like Microsoft at this point, or at least until someone gets hurt, or a Government gets taken over. Mixing modalities is also a cluttered and confusing experience. This decision will lead to disproportionate product failure and a lack of adoption in Bing once the hype dies down. This is not how you grow your 8% Bing search market share.

I hope you enjoyed this article. Hopefully, I’ve proven I’m very much alive. This has been part of a series of posts on the Responsible use of AI. For my thoughts on algorithmic bias and fairness, see this previous post.