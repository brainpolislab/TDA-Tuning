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





