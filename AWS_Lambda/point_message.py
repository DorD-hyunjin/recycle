import json
import boto3

def transform(event):
    """
    Json 파일 변환
    """
    message = event['body']
    message2 = json.dumps(message)
    return json.loads(message2)

def lambda_handler(event, context):
    """
    Json 파일 데이터에 따라
    고객 또는 관리자에게 문자 발송
    """
    message3 = transform(event)

    try:
        message3['container']
        phone_number = message3['phone_number']
        container = message3['container']
        info = '관리자님 {}함 적재가 초과되었습니다! 비워주세요:)'.format(container)
    except:
        message3 = transform(event)
        phone_number = message3['phone_number']
        point = message3['point']
        sum_points = message3['sum_points']
        info = '{}님의 에코머니 {}점 적립완료!'.format(phone_number[-4:], point) + ' ' + '(누적 포인트:{}점 /'.format(sum_points) + ' ' + '1,000점 부터 사용가능)'

    sns = boto3.client('sns')

    try:
        response = sns.publish(PhoneNumber='+82'+phone_number[1:], Message=info)
        message_id = response['MessageId']
        print('Published message to {}'.format(phone_number))
    except:
        print("Couldn't publish message to".format(phone_number))
    return {
        'statusCode': '200',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': 'publish success',
        'isBase64Encoded': 'false'
    }