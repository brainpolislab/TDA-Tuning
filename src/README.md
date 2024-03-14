# **TDA Mapper Cover Parameters Tuning with Netsimile Distance**
`tda_cover_parameters_tuning` provides functionalities for tuning Cover parameters in Topological Data Analysis (TDA) Mapper and evaluating the stability of the resulting TDA graphs using NetSimile distance metric.

### **Classes**
- **CoverTuning:** this class facilitates a grid search over user-specified ranges of _resolution_ and _gain_ values for the Cover. It creates bootstrap samples from the input data, generates TDA Mapper graphs for each combination of Cover parameters on the bootstrap samples, and computes the average NetSimile distance between the graphs.
- **GraphProperties:** this class inherits from `CoverTuning` and is designed to calculate statistical properties of a TDA graph based on fixed Cover parameters (_resolution_ and _gain_). It utilizes the NetSimile library to extract features and compute a signature of the graph, and then summarizes these features with various statistical measures (mean, median, standard deviation, skewness, and kurtosis).

### **Functionalities**
- **Grid Search for Cover Parameters:** the `grid_search` function within `CoverTuning` conducts a grid search over Cover parameter ranges and computes the average graph distance between the resulting TDA graphs using NetSimile.
- **Bootstrap Sampling:** the `get_bootstrap_sample` function generates a collection of bootstrap samples from the input dataset to assess the stability of the TDA Mapper results.
- **TDA Graph Creation:** the `create_tda_graph` function constructs a TDA Mapper graph based on the input data and specified Cover parameters.
- **Graph Distance with Netsimile:** the `graph_distance_metric` function calculates the average NetSimile distance between a list of NetworkX graphs.
- **Graph Property Statistics:** the `graph_properties_stats` function within `GraphProperties` calculates various statistical properties of a TDA graph based on the provided Cover parameters.
