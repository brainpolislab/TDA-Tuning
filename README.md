# TDA-Tuning
Topological Data Analysis (TDA) is an advanced approach to data analysis grounded in algebraic topology. It goes beyond traditional statistics by employing topological concepts to reveal inherent shapes and structures within complex datasets. Using tools like persistent homology, TDA helps identify essential topological features, offering a formal and mathematical framework for a deeper understanding of intricate data patterns.

---

## Mapper Algorithm
The Mapper algorithm plays a crucial role in TDA. Rooted in algebraic topology, Mapper is designed to reveal the Underlying structure of high-dimensional data. Using a formalized process that constructs *simplicial complex*, Mapper transforms raw data into a simplified representation, preserving essential topological information. This formal approach ensures a systematic exploration of data patterns, enhancing our understanding of intrinsic shapes and connections. 

![Mapper Algorithm Scheme](./Images/Mapper_Algorithm.png)

### 1. Filtering
This operation serves as the initial stage in the algorithm, where it transforms the original data into a format suitable for further topological analysis. In this process, a filter function, also called lens function is applied to the dataset, projecting the data points from a high-dimensional representation to a smaller one. The choice of the filter function depends on the specific characteristics and objective of the analysis, as it aims to capture essential features or attribute of the data.

### 2. Covering
This operation is a critical step for simplifying high-dimensional data representation. It involves dividing the data space into overlapping intervals, or bins, associating each with a node in the TDA graph. This approach captures local structures, enhancing the algorithm ability to understand intricate data topology. By focusing on these covers, Mapper provides a nuanced representation, preserving essential information while reducing complexity.  
Covering process is governed by two key parameters: *resolution* and *gain*. The resolution regulates the number and size of intervals in the cover, while the gain controls the size of the overlap of these intervals.

### 3. Clustering
During this operation, projected points from the high-dimensional space are grouped into clusters within each bin. These clusters become nodes in the TDA graph, representing distincs data regions. Employing techniques like hierarchical clustering or k-means, this process identifies local patterns and relationships, forming a topological network that reveals the dataset underlying structure. 

---

## Tuning of Cover parameters
The parameters governing the Covering operation, namely _resolution_ and _gain_, significantly influence the ultimate representation of the TDA graph. An optimal configuration of these parameters is crucial for enhancing the quality of the graph representation. To achieve this, a method is introduced herein, integrating bootstrapping and grid search techniques. This approach aims to systematically explore various configurations of the covering parameters, with the objective of identifying the most suitable settings that yield an improved TDA graph representation. Additionally, it is crucial to underscore that this approach does not depend on specific outcomes.

### Pipeline  
_a. Parameter range definition:_ definition of two ranges of values for both _resolution_ and _gain_ parameters  
_b. Grid search:_ the subsequent steps are carried out during each iteration of the grid search  
  * Bootstrapping (with or without replacement)
  * TDA graph construction (using Mapper algorithm)
  * Graph distances computation and/or topological properties evaluation
  * Average on the total of bootstrapped graphs

    ![Hyperparameter Tuning Pipelin](./Images/hyperparameter_tuning.jpeg)

_c. Matrix generation:_ fill matrices with the average result obtained at each iteration of the grid search  
_d. Matrix analysis and parameters combination selection:_ selection of the optimal combination of cover parameters after an accurate matrix analysis

### Matrix analysis and Cover parameters combination selection
Upon the completion of matrix construction, the subsequent step entails the selection of the optimal combination of _resolution_ and _gain_ parameters. At this point, various strategies may be considered:
* **Stability strategy**  
  This approach entails the selection of graph distance metrics. In this scenario, the ultimate matrix is assembled utilizing the average graph distance metric computed during each iteration of the grid search. The optimal combination of Cover parameters is determined by the one that yields the lowest score in the matrix. This implies that, with this specific set of parameters, the graph representation remains **_stable_**.
* **Topological properties strategy**  
  In this instance, the metric of interest is one or more topological properties selected by the user. The aim in this scenario can be either to maximize or minimize the identified property. In the event of multiple topological properties, various result matrices can be generated. For instance, a singular comprehensive matrix may be compiled by averaging all the properties, or individual matrices may be created for each property. Ultimately, the optimal combination is determined by the highest or lowest score, contingent upon the user's choice of maximizing or minimizing the property of interest.
* **Composite index strategy**  
  This strategy merges the two approaches delineated above. In this instance, distance metrics and matrices representing topological properties are integrated to derive a final matrix of scores. This final matrix serves as the basis for selecting the optimal combination of Cover parameters.

Please note that, for the latter two strategies, an optimal normalization of the final matrices is imperative to facilitate the combination of matrices associated with different metrics.

---

## fMRI data example


