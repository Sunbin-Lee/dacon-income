for %%l in (0.2, 0.1, 0.05) do (
    for %%n in (100, 200, 500) do (
        for %%d in (3, 4, 5) do (
            for %%s in (6, 8, 10) do (
                for %%f in (6, 8, 10) do (
                    python main_gbr.py --learning_rate %%l --n_estimators %%n --max_depth %%d --min_samples_split %%s --min_samples_leaf %%f
                )
            )
        )
    )

)