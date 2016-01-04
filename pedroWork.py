from csv import DictReader

filename = "vine_meta_data.csv"


def getCommentFromColumncsv(comment):
    index = 0
    while index >= 0:
        try:
            index = comment.index("#0066CC")
            comment = comment[index+9:]
        except Exception:
            break
    if "font" in comment:
        index = comment.index("font")
        comment =  comment[index+5:].strip()
    index = comment.index("(created_at")
    commentText = comment[:index]
    commentTime = comment[index+12:len(comment)-1]
    return (commentText, commentTime)


allData = []
rows = DictReader(open(filename, 'Ur'))
for ii in rows:
    commentsList = []
    postShareUrl = ii["postShareUrl"]
    postUsername = ii["postUserName"]
    for key in ii.keys():
        if "column" in key and ii[key] != "empty" and "font" in ii[key] and "created_at" in ii[key]:
            comment = getCommentFromColumncsv(ii[key])  # (commenttext,createdtime) tuple for each comment
            commentsList.append(comment)  # list of the comments for this media
    commentDataTuple = (postShareUrl, postUsername, commentsList)  # tuple of the media url, media owner and all the comments
    
    allData.append(commentDataTuple)  # total media tuples
    

print(len(allData))

print("done")
