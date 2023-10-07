import db
import analysis
import sys

def main():
    count_ids = db.post_count()
    for id in range(1, count_ids + 1):
        post = db.select_post(id)
        if post != "":
            label = analysis.analysis_data(post)[0]['label']

        check_label = db.select_label(id)[0]
        if not check_label:
            print(id, label)
            db.insert_label(label, id)
        else:
            print(id, check_label)

if __name__=="__main__":
    main()
