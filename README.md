# ProjetoRedesNeurais
Projeto final da cadeira de Redes Neurais do CIn-UFPE

## Modelos a serem testados 

# Link para o download dos arquivos do dataset (grandes demais para o git): https://drive.google.com/drive/folders/1yHxsAtF_SaDcAe3g1T7Yv3UVecnzE7Y3?usp=share_link

### MLP

Parâmetros: Layers (1,2), Neuronios (64, 128), Otimização (Adam, Drop-out, Regularização)

*Também deve ser verificado com Ensemble de MLPs

### Random Forest

Parâmetros: Criterio (gini, entropy, log_loss), n_estimators (50, 100, 150), min_sample_split (1, 2, 3), min_sample_leaf (1, 2, 3), max_feature (int, float, sqrt, log2)

### Gradient Boosting

Parâmetros: Learning_rate (0.01, 0.05, 0.1), n_estimators (50, 100, 150), Critério (friedman_mse, squared_error), min_sample_split (1, 2, 3), min_sample_leaf (1, 2, 3), max_feature (sqrt, log2)
