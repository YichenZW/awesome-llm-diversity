# Awesome LLM Diversity
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated collection of research papers exploring **diversity in Large Language Model text generation**.
This repository tracks cutting-edge research on methods, evaluation, annalysis, and application. Research from all relative domains are welcome!


**🤝 Contributing**

We welcome contributions! If you know of important papers that should be included, please:

1. Fork this repository
2. Add the paper URL to the appropriate category
3. Submit a pull request

**⭐ Support**

If you find this collection useful, please consider starring, following for updates, and sharing with others!

**🛠️ Maintenance**

This repository is built and maintained using the [automatic maintainer](https://github.com/YichenZW/awesome-paperlist-maintainer). New papers are added regularly after manual auditing to ensure comprehensive coverage of the field.


## Methodology

### Decoding

* **Flaming-hot Initiation with Regular Execution Sampling for Large Language Models** [[paper](http://arxiv.org/abs/2410.21236)] 2024-10  
      Weizhe Chen, Zhicheng Zhang, Guanlin Liu, Renjie Zheng, Wenlei Shi, Chen Dun, Zheng Wu, Xing Jin, Lin Yan.

* **PAD: Personalized Alignment of LLMs at Decoding-Time** [[paper](http://arxiv.org/abs/2410.04070)] 2024-10  
      Ruizhe Chen, Xiaotian Zhang, Meng Luo, Wenhao Chai, Zuozhu Liu. **ICLR 2025**.

  Keywords: Personalization.

* **Chain-of-Thought Reasoning Without Prompting** [[paper](http://arxiv.org/abs/2402.10200)] 2024-02  
      Xuezhi Wang, Denny Zhou.

  Keywords: Reasoning, CoT.

* **Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models** [[paper](http://arxiv.org/abs/1610.02424)] 2016-10  
      Ashwin K Vijayakumar, Michael Cogswell, Ramprasath R. Selvaraju, Qing Sun, Stefan Lee, David Crandall, Dhruv Batra. **AAAI 2018**.

### Finetuning

* **Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time** [[paper](http://arxiv.org/abs/2203.05482)] 2022-03  
      Mitchell Wortsman, Gabriel Ilharco, Samir Yitzhak Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes, Ari S. Morcos, Hongseok Namkoong, Ali Farhadi, Yair Carmon, Simon Kornblith, Ludwig Schmidt. **ICML 2022**.

* **A Distributional Approach to Controlled Text Generation** [[paper](http://arxiv.org/abs/2012.11635)] 2020-12  
      Muhammad Khalifa, Hady Elsahar, Marc Dymetman. **ICLR 2021**.

### Reinforcement Learning

* **Creative Preference Optimization** [[paper](http://arxiv.org/abs/2505.14442)] 2025-05  
      Mete Ismayilzada, Antonio Laverghetta Jr., Simone A. Luchini, Reet Patel, Antoine Bosselut, Lonneke van der Plas, Roger Beaty.

* **Modifying Large Language Model Post-Training for Diverse Creative Writing** [[paper](http://arxiv.org/abs/2503.17126)] 2025-03  
      John Joon Young Chung, Vishakh Padmakumar, Melissa Roemmele, Yuqian Sun, Max Kreminski.

* **Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF** [[paper](http://arxiv.org/abs/2312.08358)] 2023-12  
      Anand Siththaranjan, Cassidy Laidlaw, Dylan Hadfield-Menell. **ICLR 2024**.

* **Iteratively Learn Diverse Strategies with State Distance Information** [[paper](http://arxiv.org/abs/2310.14509)] 2023-10  
      Wei Fu, Weihua Du, Jingwei Li, Sunli Chen, Jingzhao Zhang, Yi Wu.

* **Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints** [[paper](http://arxiv.org/abs/2309.16240)] 2023-09  
      Chaoqi Wang, Yibo Jiang, Chenghao Yang, Han Liu, Yuxin Chen.

* **Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards** [[paper](http://arxiv.org/abs/2306.04488)] 2023-06  
      Alexandre Ramé, Guillaume Couairon, Mustafa Shukor, Corentin Dancette, Jean-Baptiste Gaya, Laure Soulier, Matthieu Cord.

* **Aligning Language Models with Preferences through f-divergence Minimization** [[paper](http://arxiv.org/abs/2302.08215)] 2023-02  
      Dongyoung Go, Tomasz Korbak, Germán Kruszewski, Jos Rozen, Nahyeon Ryu, Marc Dymetman.



* **Optimizing Temperature for Language Models with Multi-Sample Inference** [[paper](http://arxiv.org/abs/2502.05234)] 2025-02  
      Weihua Du, Yiming Yang, Sean Welleck.

  Keywords: Temperature.

* **SimpleStrat: Diversifying Language Model Generation with Stratification** [[paper](http://arxiv.org/abs/2410.09038)] 2024-10  
      Justin Wong, Yury Orlovskiy, Michael Luo, Sanjit A. Seshia, Joseph E. Gonzalez.

* **Improving Diversity of Commonsense Generation by Large Language Models via In-Context Learning** [[paper](http://arxiv.org/abs/2404.16807)] 2024-04  
      Tianhui Zhang, Bei Peng, Danushka Bollegala. **EMNLP 2024**.

* **Forcing Diffuse Distributions out of Language Models** [[paper](http://arxiv.org/abs/2404.10859)] 2024-04  
      Yiming Zhang, Avi Schwarzschild, Nicholas Carlini, Zico Kolter, Daphne Ippolito.

  Keywords: Randomness.

* **Partially Randomizing Transformer Weights for Dialogue Response Diversity** [[paper](http://arxiv.org/abs/2311.10943)] 2023-11  
      Jing Yang Lee, Kong Aik Lee, Woon-Seng Gan.

  Keywords: Framework.

* **Improving Diversity of Demographic Representation in Large Language Models via Collective-Critiques and Self-Voting** [[paper](http://arxiv.org/abs/2310.16523)] 2023-10  
      Preethi Lahoti, Nicholas Blumm, Xiao Ma, Raghavendra Kotikalapudi, Sahitya Potluri, Qijun Tan, Hansa Srinivasan, Ben Packer, Ahmad Beirami, Alex Beutel, Jilin Chen. **EMNLP 2023**.

* **Enhancing Large Language Models Against Inductive Instructions with Dual-critique Prompting** [[paper](http://arxiv.org/abs/2305.13733)] 2023-05  
      Rui Wang, Hongru Wang, Fei Mi, Yi Chen, Boyang Xue, Kam-Fai Wong, Ruifeng Xu.

* **Diversify and Disambiguate: Learning From Underspecified Data** [[paper](http://arxiv.org/abs/2202.03418)] 2022-02  
      Yoonho Lee, Huaxiu Yao, Chelsea Finn. **ICLR 2023**.

## Measurement and Analysis



* **Base Models Beat Aligned Models at Randomness and Creativity** [[paper](http://arxiv.org/abs/2505.00047)] 2025-04  
      Peter West, Christopher Potts.

* **NoveltyBench: Evaluating Language Models for Humanlike Diversity** [[paper](http://arxiv.org/abs/2504.05228)] 2025-04  
      Yiming Zhang, Harshita Diddee, Susan Holm, Hanchen Liu, Xinyue Liu, Vinay Samuel, Barry Wang, Daphne Ippolito.

  Keywords: Benchmark.

* **(How) Can Transformers Predict Pseudo-Random Numbers?** [[paper](http://arxiv.org/abs/2502.10390)] 2025-02  
      Tao Tao, Darshil Doshi, Dayal Singh Kalra, Tianyu He, Maissam Barkeshli.

  Keywords: Randomness.

* **Every Answer Matters: Evaluating Commonsense with Probabilistic Measures** [[paper](http://arxiv.org/abs/2406.04145)] 2024-06  
      Qi Cheng, Michael Boratko, Pranay Kumar Yelugam, Tim O'Gorman, Nalini Singh, Andrew McCallum, Xiang Lorraine Li. **ACL 2024**.

* **What Evidence Do Language Models Find Convincing?** [[paper](http://arxiv.org/abs/2402.11782)] 2024-02  
      Alexander Wan, Eric Wallace, Dan Klein. **ACL 2024**.

* **Exploring Precision and Recall to assess the quality and diversity of LLMs** [[paper](http://arxiv.org/abs/2402.10693)] 2024-02  
      Florian Le Bronnec, Alexandre Verine, Benjamin Negrevergne, Yann Chevaleyre, Alexandre Allauzen. **ACL 2024**.

* **Measurement in the Age of LLMs: An Application to Ideological Scaling** [[paper](http://arxiv.org/abs/2312.09203)] 2023-12  
      Sean O'Hagan, Aaron Schein. **NeurIPS 2023**.

* **The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text** [[paper](http://arxiv.org/abs/2311.09807)] 2023-11  
      Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, Chloé Clavel. **ACL 2024**.

  Keywords: Data Synthesis.

* **Understanding the Effects of RLHF on LLM Generalisation and Diversity** [[paper](http://arxiv.org/abs/2310.06452)] 2023-10  
      Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu.

* **DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks** [[paper](http://arxiv.org/abs/2309.17167)] 2023-09  
      Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie. **ICLR 2024**.

  Keywords: Reasoning.

* **Art or Artifice? Large Language Models and the False Promise of Creativity** [[paper](http://arxiv.org/abs/2309.14556)] 2023-09  
      Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, Chien-Sheng Wu. **CHI 2024**.

* **Evaluating the Moral Beliefs Encoded in LLMs** [[paper](http://arxiv.org/abs/2307.14324v1)] 2023-07  
      Nino Scherrer, Claudia Shi, Amir Feder, David M. Blei.

* **Towards Measuring the Representation of Subjective Global Opinions in Language Models** [[paper](http://arxiv.org/abs/2306.16388)] 2023-06  
      Esin Durmus, Karina Nguyen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, Liane Lovitt, Sam McCandlish, Orowa Sikder, Alex Tamkin, Janel Thamkul, Jared Kaplan, Jack Clark, Deep Ganguli.

  Keywords: Question Answering, Dataset.

* **Generating with Confidence: Uncertainty Quantification for Black-box Large Language Models** [[paper](http://arxiv.org/abs/2305.19187)] 2023-05  
      Zhen Lin, Shubhendu Trivedi, Jimeng Sun.

* **ChatGPT to Replace Crowdsourcing of Paraphrases for Intent Classification: Higher Diversity and Comparable Model Robustness** [[paper](http://arxiv.org/abs/2305.12947)] 2023-05  
      Jan Cegin, Jakub Simko, Peter Brusilovsky. **EMNLP 2023**.

* **What Comes Next? Evaluating Uncertainty in Neural Text Generators Against Human Production Variability** [[paper](http://arxiv.org/abs/2305.11707)] 2023-05  
      Mario Giulianelli, Joris Baan, Wilker Aziz, Raquel Fernández, Barbara Plank. **EMNLP 2023**.

* **Pragmatically Appropriate Diversity for Dialogue Evaluation** [[paper](http://arxiv.org/abs/2304.02812)] 2023-04  
      Katherine Stasaski, Marti A. Hearst.

* **Language Model Crossover: Variation through Few-Shot Prompting** [[paper](http://arxiv.org/abs/2302.12170)] 2023-02  
      Elliot Meyerson, Mark J. Nelson, Herbie Bradley, Adam Gaier, Arash Moradi, Amy K. Hoover, Joel Lehman.

* **Measuring and Improving Semantic Diversity of Dialogue Generation** [[paper](http://arxiv.org/abs/2210.05725)] 2022-10  
      Seungju Han, Beomsu Kim, Buru Chang.

* **Semantic Diversity in Dialogue with Natural Language Inference** [[paper](http://arxiv.org/abs/2205.01497)] 2022-05  
      Katherine Stasaski, Marti A. Hearst. **ACL 2022**.

* **Unifying Human and Statistical Evaluation for Natural Language Generation** [[paper](http://arxiv.org/abs/1904.02792)] 2019-04  
      Tatsunori B. Hashimoto, Hugh Zhang, Percy Liang.

## Alignment



* **SPARTA ALIGNMENT: Collectively Aligning Multiple Language Models through Combat** [[paper](http://arxiv.org/abs/2506.04721)] 2025-06  
      Yuru Jiang, Wenxuan Ding, Shangbin Feng, Greg Durrett, Yulia Tsvetkov.

* **Preference Optimization with Multi-Sample Comparisons** [[paper](http://arxiv.org/abs/2410.12138)] 2024-10  
      Chaoqi Wang, Zhuokai Zhao, Chen Zhu, Karthik Abinav Sankararaman, Michal Valko, Xuefei Cao, Zhaorun Chen, Madian Khabsa, Yuxin Chen, Hao Ma, Sinong Wang.

* **Can Language Models Reason about Individualistic Human Values and Preferences?** [[paper](http://arxiv.org/abs/2410.03868)] 2024-10  
      Liwei Jiang, Taylor Sorensen, Sydney Levine, Yejin Choi. **ACL 2025**.

* **Aligning to Thousands of Preferences via System Message Generalization** [[paper](http://arxiv.org/abs/2405.17977)] 2024-05  
      Seongyun Lee, Sue Hyun Park, Seungone Kim, Minjoon Seo. **NeurIPS 2024**.

* **Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback** [[paper](http://arxiv.org/abs/2404.10271)] 2024-04  
      Vincent Conitzer, Rachel Freedman, Jobst Heitzig, Wesley H. Holliday, Bob M. Jacobs, Nathan Lambert, Milan Mossé, Eric Pacuit, Stuart Russell, Hailey Schoelkopf, Emanuel Tewolde, William S. Zwicker.

* **MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models** [[paper](http://arxiv.org/abs/2403.17141)] 2024-03  
      Kailai Yang, Zhiwei Liu, Qianqian Xie, Jimin Huang, Tianlin Zhang, Sophia Ananiadou. **NeurIPS 2024**.

* **Evaluating Agents using Social Choice Theory** [[paper](http://arxiv.org/abs/2312.03121)] 2023-12  
      Marc Lanctot, Kate Larson, Yoram Bachrach, Luke Marris, Zun Li, Avishkar Bhoopchand, Thomas Anthony, Brian Tanner, Anna Koop.

* **AI Alignment and Social Choice: Fundamental Limitations and Policy Implications** [[paper](http://arxiv.org/abs/2310.16048)] 2023-10  
      Abhilash Mishra.

* **The Empty Signifier Problem: Towards Clearer Paradigms for Operationalising "Alignment" in Large Language Models** [[paper](http://arxiv.org/abs/2310.02457)] 2023-10  
      Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, Scott A. Hale.

* **Everyone Deserves A Reward: Learning Customized Human Preferences** [[paper](http://arxiv.org/abs/2309.03126)] 2023-09  
      Pengyu Cheng, Jiawen Xie, Ke Bai, Yong Dai, Nan Du.

## Pluralism



* **Biased AI can Influence Political Decision-Making** [[paper](http://arxiv.org/abs/2410.06415)] 2024-10  
      Jillian Fisher, Shangbin Feng, Robert Aron, Thomas Richardson, Yejin Choi, Daniel W. Fisher, Jennifer Pan, Yulia Tsvetkov, Katharina Reinecke.

* **From Distributional to Overton Pluralism: Investigating Large Language Model Alignment** [[paper](http://arxiv.org/abs/2406.17692)] 2024-06  
      Thom Lake, Eunsol Choi, Greg Durrett. **ACL 2025**.

* **Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration** [[paper](http://arxiv.org/abs/2406.15951)] 2024-06  
      Shangbin Feng, Taylor Sorensen, Yuhan Liu, Jillian Fisher, Chan Young Park, Yejin Choi, Yulia Tsvetkov. **EMNLP 2024**.

* **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models** [[paper](http://arxiv.org/abs/2404.16019)] 2024-04  
      Hannah Rose Kirk, Alexander Whitefield, Paul Röttger, Andrew Bean, Katerina Margatina, Juan Ciro, Rafael Mosquera, Max Bartolo, Adina Williams, He He, Bertie Vidgen, Scott A. Hale.

* **The PRISM Alignment Dataset: What Participatory, Representative and Individualised Human Feedback Reveals About the Subjective and Multicultural Alignment of Large Language Models** [[paper](http://arxiv.org/abs/2404.16019)] 2024-04  
      Hannah Rose Kirk, Alexander Whitefield, Paul Röttger, Andrew Bean, Katerina Margatina, Juan Ciro, Rafael Mosquera, Max Bartolo, Adina Williams, He He, Bertie Vidgen, Scott A. Hale.

  Keywords: Dataset.

* **A Roadmap to Pluralistic Alignment** [[paper](http://arxiv.org/abs/2402.05070)] 2024-02  
      Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, Tim Althoff, Yejin Choi. **ICML 2024**.

* **How Far Can We Extract Diverse Perspectives from Large Language Models?** [[paper](http://arxiv.org/abs/2311.09799)] 2023-11  
      Shirley Anugrah Hayati, Minhwa Lee, Dheeraj Rajagopal, Dongyeop Kang. **EMNLP 2024**.

* **Improving Diversity of Demographic Representation in Large Language Models via Collective-Critiques and Self-Voting** [[paper](http://arxiv.org/abs/2310.16523)] 2023-10  
      Preethi Lahoti, Nicholas Blumm, Xiao Ma, Raghavendra Kotikalapudi, Sahitya Potluri, Qijun Tan, Hansa Srinivasan, Ben Packer, Ahmad Beirami, Alex Beutel, Jilin Chen. **EMNLP 2023**.

* **Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties** [[paper](http://arxiv.org/abs/2309.00779)] 2023-09  
      Taylor Sorensen, Liwei Jiang, Jena Hwang, Sydney Levine, Valentina Pyatkin, Peter West, Nouha Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavatula, Maarten Sap, John Tasioulas, Yejin Choi.

* **Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias** [[paper](http://arxiv.org/abs/2306.15895)] 2023-06  
      Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng, Alexander Ratner, Ranjay Krishna, Jiaming Shen, Chao Zhang. **NeurIPS 2023**.

* **Whose Opinions Do Language Models Reflect?** [[paper](http://arxiv.org/abs/2303.17548)] 2023-03  
      Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, Tatsunori Hashimoto.

## Application



* **Evaluating Cultural and Social Awareness of LLM Web Agents** [[paper](http://arxiv.org/abs/2410.23252)] 2024-10  
      Haoyi Qiu, Alexander R. Fabbri, Divyansh Agarwal, Kung-Hsiang Huang, Sarah Tan, Nanyun Peng, Chien-Sheng Wu. **ACL 2025**.

  Keywords: Web Agent, Benchmark.

* **Benchmarking Language Model Creativity: A Case Study on Code Generation** [[paper](http://arxiv.org/abs/2407.09007)] 2024-07  
      Yining Lu, Dixuan Wang, Tianjian Li, Dongwei Jiang, Sanjeev Khudanpur, Meng Jiang, Daniel Khashabi.

  Keywords: Code Generation.

* **GenQA: Generating Millions of Instructions from a Handful of Prompts** [[paper](http://arxiv.org/abs/2406.10323)] 2024-06  
      Jiuhai Chen, Rifaa Qadri, Yuxin Wen, Neel Jain, John Kirchenbauer, Tianyi Zhou, Tom Goldstein.

  Keywords: Data Synthesis.

* **SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents** [[paper](http://arxiv.org/abs/2310.11667)] 2023-10  
      Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, Maarten Sap.

  Keywords: Multi Agent.

* **Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias** [[paper](http://arxiv.org/abs/2306.15895)] 2023-06  
      Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng, Alexander Ratner, Ranjay Krishna, Jiaming Shen, Chao Zhang. **NeurIPS 2023**.

  Keywords: Data Synthesis.

## Other



* **Uncertainty in Natural Language Generation: From Theory to Applications** [[paper](http://arxiv.org/abs/2307.15703)] 2023-07  
      Joris Baan, Nico Daheim, Evgenia Ilia, Dennis Ulmer, Haau-Sing Li, Raquel Fernández, Barbara Plank, Rico Sennrich, Chrysoula Zerva, Wilker Aziz.

  Keywords: Survey.

* **Convergence Voting: From Pairwise Comparisons to Consensus** [[paper](http://arxiv.org/abs/2102.01995)] 2021-02  
      Gergei Bana, Wojciech Jamroga, David Naccache, Peter Y. A. Ryan.

  Keywords: Voting Theory.

* **Rank Centrality: Ranking from Pair-wise Comparisons** [[paper](http://arxiv.org/abs/1209.1688)] 2012-09  
      Sahand Negahban, Sewoong Oh, Devavrat Shah.

  Keywords: Ranking Algorithm.

## Human-Centered Analysis and Application



* **Does Writing with Language Models Reduce Content Diversity?** [[paper](http://arxiv.org/abs/2309.05196)] 2023-09  
      Vishakh Padmakumar, He He. **ICLR 2024**.

* **Artificial Artificial Artificial Intelligence: Crowd Workers Widely Use Large Language Models for Text Production Tasks** [[paper](http://arxiv.org/abs/2306.07899)] 2023-06  
      Veniamin Veselovsky, Manoel Horta Ribeiro, Robert West.

* **Factors Influencing Perceived Fairness in Algorithmic Decision-Making: Algorithm Outcomes, Development Procedures, and Individual Differences** [[paper](http://arxiv.org/abs/2001.09604)] 2020-01  
      Ruotong Wang, F. Maxwell Harper, Haiyi Zhu. **CHI 2020**.

## Multi-Culture and Multi-Lingual Application



* **CARE: Assessing the Impact of Multilingual Human Preference Learning on Cultural Awareness** [[paper](http://arxiv.org/abs/2504.05154)] 2025-04  
      Geyang Guo, Tarek Naous, Hiromi Wakaki, Yukiko Nishimura, Yuki Mitsufuji, Alan Ritter, Wei Xu.

* **CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming** [[paper](http://arxiv.org/abs/2410.02677)] 2024-10  
      Yu Ying Chiu, Liwei Jiang, Bill Yuchen Lin, Chan Young Park, Shuyue Stella Li, Sahithya Ravi, Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov, Vered Shwartz, Yejin Choi. **ACL 2025**.

  Keywords: Benchmark.

* **CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models** [[paper](http://arxiv.org/abs/2405.13974)] 2024-05  
      Giada Pistilli, Alina Leidinger, Yacine Jernite, Atoosa Kasirzadeh, Alexandra Sasha Luccioni, Margaret Mitchell.

  Keywords: Benchmark.

* **CultureBank: An Online Community-Driven Knowledge Base Towards Culturally Aware Language Technologies** [[paper](http://arxiv.org/abs/2404.15238)] 2024-04  
      Weiyan Shi, Ryan Li, Yutong Zhang, Caleb Ziems, Chunhua yu, Raya Horesh, Rogério Abreu de Paula, Diyi Yang.

* **EtiCor: Corpus for Analyzing LLMs for Etiquettes** [[paper](http://arxiv.org/abs/2310.18974)] 2023-10  
      Ashutosh Dwivedi, Pradhyumna Lavania, Ashutosh Modi. **EMNLP 2023**.

* **Global Voices, Local Biases: Socio-Cultural Prejudices across Languages** [[paper](http://arxiv.org/abs/2310.17586)] 2023-10  
      Anjishnu Mukherjee, Chahat Raj, Ziwei Zhu, Antonios Anastasopoulos. **EMNLP 2023**.

* **CulturaX: A Cleaned, Enormous, and Multilingual Dataset for Large Language Models in 167 Languages** [[paper](http://arxiv.org/abs/2309.09400)] 2023-09  
      Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A. Rossi, Thien Huu Nguyen.

* **BHASA: A Holistic Southeast Asian Linguistic and Cultural Evaluation Suite for Large Language Models** [[paper](http://arxiv.org/abs/2309.06085)] 2023-09  
      Wei Qi Leong, Jian Gang Ngui, Yosephine Susanto, Hamsawardhini Rengarajan, Kengatharaiyer Sarveswaran, William Chandra Tjhi.

* **SeaEval for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning** [[paper](http://arxiv.org/abs/2309.04766)] 2023-09  
      Bin Wang, Zhengyuan Liu, Xin Huang, Fangkai Jiao, Yang Ding, AiTi Aw, Nancy F. Chen. **ACL 2024**.

* **Multi-lingual and Multi-cultural Figurative Language Understanding** [[paper](http://arxiv.org/abs/2305.16171)] 2023-05  
      Anubha Kabra, Emmy Liu, Simran Khanuja, Alham Fikri Aji, Genta Indra Winata, Samuel Cahyawijaya, Anuoluwapo Aremu, Perez Ogayo, Graham Neubig. **ACL 2023**.

* **SeeGULL: A Stereotype Benchmark with Broad Geo-Cultural Coverage Leveraging Generative Models** [[paper](http://arxiv.org/abs/2305.11840)] 2023-05  
      Akshita Jha, Aida Davani, Chandan K. Reddy, Shachi Dave, Vinodkumar Prabhakaran, Sunipa Dev.

  Keywords: Benchmark.

* **EnCBP: A New Benchmark Dataset for Finer-Grained Cultural Background Prediction in English** [[paper](http://arxiv.org/abs/2203.14498)] 2022-03  
      Weicheng Ma, Samiha Datta, Lili Wang, Soroush Vosoughi. **ACL 2022**.

  Keywords: Benchmark.

* **Challenges and Strategies in Cross-Cultural NLP** [[paper](http://arxiv.org/abs/2203.10020)] 2022-03  
      Daniel Hershcovich, Stella Frank, Heather Lent, Miryam de Lhoneux, Mostafa Abdou, Stephanie Brandl, Emanuele Bugliarello, Laura Cabello Piqueras, Ilias Chalkidis, Ruixiang Cui, Constanza Fierro, Katerina Margatina, Phillip Rust, Anders Søgaard. **ACL 2022**.

