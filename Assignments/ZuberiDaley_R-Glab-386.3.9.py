import pandas as pd
# Business Team
BTData = {
    'Name': ['Zuberi', 'Bob', 'Charlie', 'Alice'],
    'Age': [30, 30, 28, 24],
    'Department': ['CEO','IT','Finance','HR'],
    'AI Agents Team': ['Jarvis', 'Tech Stuff Pod', 'PocketWatcher Pod', 'Dont Get Fired Pod' ]
}
df = pd.DataFrame(BTData)
print(df)