<h2>File/Folder Descriptions</h2>

**Project Notes:** Where thoughts and progress on the project is logged by date. This way, ideas from a work session aren't lost. What bugs were fixed? What details need to be fixed in the future? Are there conceptual problems discovered that need more attention? 

**build_coauthor_network.py:** Script that reads in CDC dataset and returns a coauthorship network 

**Reference Papers:** Where papers relevant to the project are kept. These papers will be source material for the literature review, but also will point to useful methods and tools. 

**collaboration_infrastructure.txt:** Where logistical stuff is dealt with. Right now contains link to google doc for project drafting. 

**COVID19_Sample_Dataset_1.xlsx:** Self-explanatory file title.     

<h2>HYPOTHESIS: It is possible to predict the quality or influence of a newly published research paper on COVID19.</h2> 

The CDC publishes datasets of research papers concerning COVID19. These datasets can be used for two potentially complementary project components.   

**Components and Options:** 

1. *ML classifier of papers as high or low quality:* Will take as input a training set of papers and predict the quality of a new paper (good or bad). Or, papers can be automatically scored using their features. Then a regression model can be applied to predict the “quality” of a new paper. In either case, an opportunity for novelty is introduced, whereby a feature set relevant to the quality of a paper is generated after review of papers widely considered influential and papers considered low grade. A significant effort would have to be directed towards data extraction for the agreed upon feature set. A regression model could also be constructed using the citation impact of a paper to predict influence (in terms of citation impact) of a new paper.  

2. *Paper coauthorship network:* Here we want to ask how the coauthorship network can be used to compliment the classifier, either through validation or application. In the case of validation, techniques already exist within the closed set of ML techniques for validation. The only prerequisite is a sufficient amount of labeled data. 

**The need for a novel method for classifying paper quality:** 

*Using the coauthor network for ML prediction validation:* If authors are characterized by citation impact as a proxy for reputation, then the nodes representing them can accordingly be given scores (for example, if the score of each node is the average score of its neighbors). Various regions of the network can then be characterized by the average local (ill-defined right now) node score. This can be visualized as a color gradient -- dark red = high score vs light red = low score, for example. Papers can then be plotted on the network equidistant from each of its coauthors. If a high quality paper appears in a region of the network characterized by a high average author influence, a dark red region that is, then the ML prediction is, in a sense, validated. This validation scheme, however, depends on the assumption that high quality papers will be authored by influential authors and low quality papers will be authored by not very influential authors. In either case, however, -- a novel feature based quality classifier or a citation-based influence predictor -- this scheme does not work. In the first case, if the assumption previously mentioned holds with high probability, then high quality papers that appear in low influence network regions become peculiar. Here, genuine examples of low influence authors (e.g, PhD students) who publish high quality work will be conflated with low quality work misclassified as high quality work. In the latter case, a paper’s citation impact is not independent of the influence of its authors. Given the information available, no network-based validation scheme obviously dissimilar to this one readily presents itself. 

*Using the coauthor network for application*: The second option, applying the predictions of the trained ML classifier to the network seems very rich. As a simple example, let QS be the “quality score” of an author, calculated as the average of the quality scores for all the papers he has (co) authored. Then, the weight W given to a node i in the network can be given by the average of the QS of authors represented by i’s neighbors. The network can then be given a “quality color gradient” to be contrasted with the “influence color gradient” previously described. Further network analysis can be done to find author clusters that produce high quality work, identify authors on the borders between high quality and low quality network regions, and even perhaps determine how likely a particular author is to publish high quality work given his position in the network.

Note that this direction not only results in a minimal viable product, but also an interesting application of it for extended analysis. 

**Plan B:**

The ML classifier depends on being able to construct a workable feature set for determining the quality of a paper. This will require some ingenuity. There is much guidance, however, from the existing literature on how to go about this. Feature sets exist for ML projects attempting to predict whether a paper will be accepted into a conference or journal, for example. If, however, this is unsuccessful, there are many options to explore related only to the coauthorship network. Again, here, much guidance in the existing literature is available. Coauthorship networks have been extensively studied. The novelty of the project would here be associated with the dataset being used. A coauthorship analysis of COVID19 research papers has not yet been conducted. This would simply be a matter of making a certain hypothesis about the COVID19 coauthorship network, then using existing network analysis tools to validate it. 

This will be particularly easy given that libraries for network analysis already exist, and I have already written a script to construct the coauthorship network from the CDC datasets. The bulk of the work will be in labeling data. Building of the CDC datasets was automated -- papers returned by keyword searches in databases were pulled and their titles, author names, abstracts, and DOIs, among other information, stripped. But, author names were not in many cases properly recorded or delimited. They need to be in order for the coauthorship network to be accurately constructed.  
