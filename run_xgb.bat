for %%n in (100, 200, 500, 1000) do (
    for %%d in (3, 4, 5, 6) do (
        for %%l in (0.3, 0.2, 0.1, 0.05) do (
            for %%m in (1, 2, 5, 10) do (
                python main_xgb.py --learning_rate %%l --n_estimators %%n --max_depth %%d --min_child_weight %%m
            )
        )
    )
)