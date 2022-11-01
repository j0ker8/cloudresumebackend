import json
import boto3
dynamodb = boto3.resource('dynamodb');
table = dynamodb.Table('visitorcounter');

def lambda_handler(event, context):
    # TODO implement
    response=table.get_item(Key={"elementid": "primary"})
    item=int(response["Item"]["vcount"]) + 1
    print(item)
    #vcount=response["vcount"];
    table.update_item(
    Key={
        "elementid": "primary"
    },
    UpdateExpression='SET vcount= :val1',
    ExpressionAttributeValues={
        ':val1': item 
    })
    
    return {
        'statusCode': 200,
        'body': item
    }
