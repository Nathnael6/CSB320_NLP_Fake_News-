# AI Review

## AI Feedback

The project follows the required NLP pipeline clearly and includes both a primary fake news dataset and a secondary cyberbullying dataset. The notebooks include preprocessing, TF-IDF feature extraction, sentiment analysis, Random Forest training, classification reports, confusion matrices, and cross-validation. Overall, the workflow is complete and easy to follow.

However, the fake news model’s 99% accuracy should be interpreted carefully. A result this high may suggest the dataset is very easy to separate, but it could also point to possible dataset bias, strong wording patterns, or hidden differences between fake and real articles. The analysis would be stronger if it questioned whether the model is truly learning misinformation patterns or simply learning dataset-specific writing style.

The cyberbullying dataset gives a more realistic view of NLP difficulty. The model performs well on the cyberbullying class but struggles with the non-cyberbullying class. This matters because false positives could unfairly label normal tweets as harmful. The binary conversion also simplifies several different cyberbullying categories into one label, which may hide important differences between types of harm.

Another limitation is that only one model was tested. Random Forest is acceptable, but NLP classification often benefits from comparing models such as Naive Bayes, Logistic Regression, or Support Vector Machines. The project would also be stronger with more tweet-specific preprocessing, such as handling usernames, hashtags, emojis, URLs, sarcasm, and repeated characters.

Overall, the project meets the assignment requirements, but the analysis should be careful not to overclaim. The fake news results are very strong, while the cyberbullying results show that real-world text classification is more complicated than accuracy alone can show.

---

## Reflection

The AI feedback made me think more critically about the very high fake news score. At first, 99% accuracy looked like a perfect result, but it may also mean the dataset has patterns that make it easier than real-world fake news detection. I agree that the cyberbullying model needs careful interpretation because false positives could unfairly label people’s tweets as harmful.
