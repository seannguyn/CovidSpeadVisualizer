# @app.route("/randomizeNoSocialDistance", methods=["GET"])
# def randomizeNoSocialDistance():
#
#     # call random function
#     randomGrid = Grid.randomInputStringAndCovidNoSocialDistance()
#
#     # write random string to a file
#     with open("noSocialDistance.txt", "a+") as file_object:
#         # Move read cursor to the start of file.
#         file_object.seek(0)
#         # If file is not empty then append '\n'
#         data = file_object.read(100)
#         if len(data) > 0:
#             file_object.write("\n")
#         # Append text at the end of file
#         file_object.write(randomGrid)
#
#     # read file
#     with open("noSocialDistance.txt") as f:
#         content = f.readlines()
#
#     # you may also want to remove whitespace characters like `\n` at the end of each line
#     content = [x.strip() for x in content]
#
#     line = content[randrange(len(content))]
#
#     virusPoints = randomGrid.split("|")[0].split("_")
#     inputString = randomGrid.split("|")[1]
#
#     gridInfo = {
#         "covid": virusPoints,
#         "inputString": inputString,
#     }
#     return jsonify(gridInfo)

# def randomizeSocialDistance():
#
#     # call random function
#     randomGrid = Grid.randomInputStringAndCovidSocialDistance()
#
#     # write random string to a file
#     with open("socialDistance.txt", "a+") as file_object:
#         # Move read cursor to the start of file.
#         file_object.seek(0)
#         # If file is not empty then append '\n'
#         data = file_object.read(100)
#         if len(data) > 0:
#             file_object.write("\n")
#         # Append text at the end of file
#         file_object.write(randomGrid)
#
#     # read file
#     with open("socialDistance.txt") as f:
#         content = f.readlines()
#
#     # you may also want to remove whitespace characters like `\n` at the end of each line
#     content = [x.strip() for x in content]
#
#     line = content[randrange(len(content))]
#
#     virusPoints = line.split("|")[0].split("_")
#     inputString = line.split("|")[1]
#
#     gridInfo = {
#         "covid": virusPoints,
#         "inputString": inputString,
#     }
#     return jsonify(gridInfo)