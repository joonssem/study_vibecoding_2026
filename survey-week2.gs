/**
 * Google Apps Script에서 createWeek2Survey를 한 번 실행합니다.
 * 실행 로그에서 설문 응답 링크와 편집 링크를 확인합니다.
 * 실행할 때마다 새 설문지가 만들어집니다.
 */
function createWeek2Survey() {
  const form = FormApp.create('화요일 바이브코딩 2회차 마무리 설문');
  form.setDescription('오늘의 경험을 돌아보고 3회차 준비에 활용합니다. 약 3분 정도 걸립니다. 이름과 학생 개인정보는 적지 않아도 됩니다.');
  form.setConfirmationMessage('응답해 주셔서 감사합니다.');

  form.addCheckboxItem()
    .setTitle('1. 오늘 어디까지 해 보셨나요?')
    .setHelpText('해당하는 항목을 모두 선택해 주세요.')
    .setChoiceValues([
      'OpenCode와 AI 모델 준비',
      '기존 앱을 컴퓨터로 가져오기',
      'AI에게 앱 설명 요청하기',
      '앱 수정 요청하고 결과 확인하기',
      '다시 요청해 한 번 더 고치기',
      '수정한 앱을 GitHub에 다시 올리기'
    ]);

  form.addMultipleChoiceItem()
    .setTitle('2. 오늘 앱을 고치고 확인하는 과정은 어떠셨나요?')
    .setChoiceValues([
      '혼자서도 다시 해 볼 수 있을 것 같아요',
      '안내를 참고하면 해 볼 수 있을 것 같아요',
      '도움이 더 필요해요',
      '아직 해 보지 못했어요'
    ]);

  form.addCheckboxItem()
    .setTitle('3. 어려웠던 부분은 무엇인가요?')
    .setHelpText('해당하는 항목을 모두 선택해 주세요.')
    .setChoiceValues([
      '설치 또는 AI 모델 연결',
      '저장소 가져오기 또는 폴더 열기',
      'AI에게 원하는 수정 설명하기',
      '수정 결과 확인 또는 오류 해결',
      'GitHub에 수정 내용 올리기',
      '특별히 어려운 점이 없었어요'
    ])
    .showOtherOption(true);

  form.addParagraphTextItem().setTitle('4. 오늘 고친 점이나 새롭게 알게 된 점은 무엇인가요?');
  form.addParagraphTextItem().setTitle('5. 교실에서 활용하고 싶은 방법이나 다음에 고치고 싶은 점은 무엇인가요?');
  form.addParagraphTextItem().setTitle('6. 3회차에 더 알아보거나 도움받고 싶은 내용이 있나요? (선택)');

  Logger.log('응답 링크: ' + form.getPublishedUrl());
  Logger.log('편집 링크: ' + form.getEditUrl());
}
