# import pandas as pd
# import json
# import os

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression, Ridge, Lasso
# from sklearn.svm import SVR
# from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
# from sklearn.ensemble import (RandomForestRegressor, GradientBoostingRegressor, RandomForestClassifier,
#                               GradientBoostingClassifier)
# from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler
# from entityOperation import create_table, open_read_file
# from commonUtility import logger, debug_print
# from commonUtilityTrainingModel import get_data_model, create_lag_features, get_file_name, json_converter
# from inspect import signature

# import time
# import traceback
# import joblib
# import psycopg2
# from psycopg2 import sql

# # Specify the seed for reproducibility
# random_seed = 42

# # Initialize the model based on the type you specify and Train it
# model_dict = {
#     'LinearRegression': LinearRegression(fit_intercept=True),
#     'Lasso': Lasso(random_state=random_seed),
#     'SVR': SVR(C=1.0,
#                kernel='rbf',
#                degree=3,
#                gamma='scale',
#                epsilon=0.1,
#                shrinking=True,
#                tol=1e-3,
#                cache_size=200,
#                ),
#     'DecisionTreeRegressor': DecisionTreeRegressor(criterion='squared_error',
#                                                    max_depth=10,
#                                                    min_samples_split=5,
#                                                    min_samples_leaf=2,
#                                                    max_features='sqrt',
#                                                    random_state=random_seed,
#                                                    splitter='best',
#                                                    max_leaf_nodes=None,
#                                                    min_weight_fraction_leaf=0.0,
#                                                    ),
#     'RandomForestRegressor': RandomForestRegressor(n_estimators=100,
#                                                    max_depth=10,
#                                                    min_samples_split=5,
#                                                    min_samples_leaf=2,
#                                                    max_features='sqrt',
#                                                    random_state=random_seed,
#                                                    ),
#     'GradientBoostingRegressor': GradientBoostingRegressor(n_estimators=100,
#                                                            learning_rate=0.1,
#                                                            max_depth=3,
#                                                            subsample=1.0,
#                                                            random_state=random_seed,
#                                                            ),
#     # 'KNeighborsRegressor': KNeighborsRegressor(n_neighbors=5,
#     #                                            weights='uniform',
#     #                                            algorithm='auto',
#     #                                            leaf_size=30
#     #                                            ),
#     'LogisticRegression': LogisticRegression(penalty='l2',
#                                              C=1.0,
#                                              solver='liblinear',
#                                              max_iter=500,
#                                              random_state=random_seed,
#                                              ),
#     'SVC': SVC(C=1.0,
#                kernel='rbf',
#                degree=3,
#                gamma='scale',
#                shrinking=True,
#                tol=1e-3,
#                cache_size=200,
#                ),
#     'DecisionTreeClassifier': DecisionTreeClassifier(criterion='gini',
#                                                      max_depth=None,
#                                                      min_samples_split=2,
#                                                      min_samples_leaf=1,
#                                                      max_features=None,
#                                                      random_state=random_seed,
#                                                      splitter='best',
#                                                      max_leaf_nodes=None,
#                                                      min_weight_fraction_leaf=0.0,
#                                                      ),
#     'RandomForestClassifier': RandomForestClassifier(n_estimators=100,
#                                                      max_depth=None,
#                                                      min_samples_split=2,
#                                                      min_samples_leaf=1,
#                                                      max_features=None,
#                                                      random_state=random_seed,
#                                                      ),
#     # 'GradientBoostingClassifier': GradientBoostingClassifier(n_estimators=50,
#     #                                                          learning_rate=0.1,
#     #                                                          max_depth=2,
#     #                                                          subsample=0.8,
#     #                                                          random_state=random_seed,
#     #                                                          ),
#     'KNeighborsClassifier': KNeighborsClassifier(n_neighbors=5,
#                                                  weights='uniform',
#                                                  algorithm='auto',
#                                                  leaf_size=30,
#                                                  )
# }

# # column_definitions = []
# # for model_name, model in model_dict.items():
# #     # Creating table for adding the score card
# #     column_definitions.append(sql.Identifier(model_name) + sql.SQL(" ") + sql.SQL("float"))  # + sql.SQL(" ") +
# #     column_definitions.append(sql.Identifier(model_name + "_time") + sql.SQL(" ") + sql.SQL("float"))

# # # debug_print("column_definitions: {}".format(column_definitions))
# # config = open_read_file('resources', '', 'general')
# # table_name = config['project_name_table_name']
# # create_table(table_name, column_definitions)
