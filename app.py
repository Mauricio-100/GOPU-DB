import gradio as gr
import psycopg2

def query_db(sql):
    try:
        conn = psycopg2.connect(
            dbname="gopu",
            user="ceose",
            password="agentic",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(sql)
        if sql.strip().lower().startswith("select"):
            rows = cur.fetchall()
            return "\n".join(str(row) for row in rows)
        else:
            conn.commit()
            return "✅ Requête exécutée"
    except Exception as e:
        return f"❌ Erreur : {e}"
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

gr.Interface(fn=query_db, inputs="text", outputs="text", title="🧠 GopuDB Console").launch(server_name="0.0.0.0", server_port=7860)
