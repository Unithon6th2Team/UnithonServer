import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamo.Table('todo')

    record_false = table.scan(
        FilterExpression=Attr('finished').eq(False)
    )
    count_false = len(record_false['Items'])
    record_true = table.scan(
        FilterExpression=Attr('finished').eq(True)
    )
    count_true = len(record_true['Items'])
    record_my_false = table.scan(
        FilterExpression=Attr('finished').eq(False) & Attr('target_id').eq(event['owner_id'])
    )
    count_my_false = len(record_my_false["Items"])

    response = {
        "count_false": count_false,
        "count_true": count_true,
        "count_my_false": count_my_false
    }
    return (response)

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamo.Table('todo')
    table.delete_item(Key={'id':event['id']})

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamo.Table('todo')
    response = table.scan()
    Items = response['Items']
    response2 = {"Items":Items}
    return response2

def lambda_handler(event, context):
    dynamo = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table = dynamo.Table('todo')

    for idx, value in enumerate(event):
        print(value)
        table.put_item(Item=value)
