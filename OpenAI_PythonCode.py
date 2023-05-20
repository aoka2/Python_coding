import openai

input_file = input("要約したいファイルのパス: ")
with open(input_file, encoding='utf-8') as f:
    text = f.read()
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content" : f"この文章を要約してください。「{text}」"},
    ]
)
res_content = res["choices"][0]["message"]["content"]

with open("output.txt" , "w") as f:
    f.write(res_content)


# $env:OPENAI_API_KEY="ビューAPIキーを添付"　←　環境変数を指定する







'''
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "なぜ、月は満ち欠けをするのですか？"},
        {"role": "assistant", "content": "月が満ち欠けするのは、地球と月の位置や角度が変化するためです。月が地球の周りを回るとき、太陽光線が地球と月の位置関係によって、月の表面に当たる角度や量が変わります。一定の周期で、月の表面に当たる太陽光線の割合が変化するため、月の形が変化し、満ち欠けが生じるのです。これが月相と呼ばれるものです。"},
        {"role": "user", "content": "もう少し簡潔に教えてください。"},
    ]
)

res_content = res["choices"][0]["message"]["content"]
print(res_content)
'''

