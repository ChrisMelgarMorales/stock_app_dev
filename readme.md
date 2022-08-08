#Node.js v14.x or later

#npm v6.14.4 or later

#git v2.14.1 or later

#Initialize a new React Native application. There are two ways to do this:

#Expo CLI - Easier for new React Native developers
#React Native CLI - If you are already familiar with mobile development, enables you to build native code into your project.

#clone github repository

expo init  #name:stock_app_dev #template:blank 

#copy files to cloned github folder
npm install -g @aws-amplify/cli

amplify init
amplify pull --appId d3s84mkgp5y9tm --envName staging

#PS E:\Coding\React\stock_app_dev-1> amplify pull --appId d3s84mkgp5y9tm --envName staging
#Opening link: https://us-west-1.admin.amplifyapp.com/admin/d3s84mkgp5y9tm/staging/verify/?loginVersion=1
#\ Confirm login in the browser or manually paste in your CLI login key:
#√ Successfully received Amplify Studio tokens.
#Amplify AppID found: d3s84mkgp5y9tm. Amplify App name is: stock_app_dev
#Backend environment staging found in Amplify Console app: stock_app_dev
#? Choose your default editor: Visual Studio Code
#? Choose the type of app that you're building (Use arrow keys)
#? Choose the type of app that you're building javascript  
#Please tell us about your project
#? What javascript framework are you using react-native
#? Source Directory Path:  src      
#? Distribution Directory Path: /
#? Build Command:  npm.cmd run-script build  
#? Start Command: npm.cmd run-script start
#✅ GraphQL schema compiled successfully.

#Edit your schema at E:\Coding\React\stock_app_dev-1\amplify\backend\api\stockappdev\schema.graphql or place .graphql files in a directory at #E:\Coding\React\stock_app_dev-1\amplify\backend\api\stockappdev\schema
#Successfully generated models. Generated models can be found in E:\Coding\React\stock_app_dev-1\src
#? Do you plan on modifying this backend? Yes


npm install aws-amplify aws-amplify-react-native amazon-cognito-identity-js @react-native-community/netinfo @react-native-async-storage/async-storage @react-native-picker/picker
npm install aws-amplify @react-native-community/netinfo @react-native-async-storage/async-storage
npm install aws-amplify @aws-amplify/ui-react
npm start