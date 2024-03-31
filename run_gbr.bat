@echo off

for %%l in (0.1 0.05) do (
    for %%n in (100 200 500) do (
        for %%d in (3 4 5) do (
            for %%s in (8 16 30) do (
                for %%f in (16 30) do (
                    python main_gbr.py --learning_rate %%l --n_estimators %%n --max_depth %%d --min_samples_split %%s --min_samples_leaf %%f
                )
            )
        )
    )

)