# TDA-Tuning
Topological Data Analysis (TDA) is an advanced approach to data analysis grounded in algebraic topology. It goes beyond traditional statistics by employing topological concepts to reveal inherent shapes and structures within complex datasets. Using tools like persistent homology, TDA helps identify essential topological features, offering a formal and mathematical framework for a deeper understanding of intricate data patterns.

---

## Mapper Algorithm
The Mapper algorithm plays a crucial role in TDA. Rooted in algebraic topology, Mapper is designed to reveal the Underlying structure of high-dimensional data. Using a formalized process that constructs *simplicial complex*, Mapper transforms raw data into a simplified representation, preserving essential topological information. This formal approach ensures a systematic exploration of data patterns, enhancing our understanding of intrinsic shapes and connections. 

![Mapper Algorithm Scheme](./images/Mapper_Algorithm.png)

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
  * Graph distances computation
  * Average on the total of bootstrapped graphs

    ![Hyperparameter Tuning Pipeline](./images/hyperparameter_tuning.jpeg)

_c. Matrix generation:_ fill matrices with the average result obtained at each iteration of the grid search  
_d. Matrix analysis and parameters combination selection:_ selection of the optimal combination of cover parameters after an accurate matrix analysis

#### Cover parameters combination selection
The most appropriate parameter configuration is the one that yields the lowest score within the final matrix. A smaller value signifies a more robust graph representation, especially when considering the NetSimile distance as the metric for graph distance. A minimal score indicates that the topological features remain consistent across various graphs constructed with the same Cover parameters but on different datasets, thanks to the bootstrapping methodology employed.


