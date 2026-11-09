/** 한 번 실행할 때마다 새 Google 설문지를 만듭니다. */
function createWeek2Survey() {
  const form = FormApp.create('바이브코딩 스터디 2회차 준비 설문');

  form.setDescription(
    '1회차에 함께해 주셔서 감사합니다. 2회차에서는 만든 앱을 이어서 고치고, AI 에이전트와 개인정보·공개 원칙을 살펴볼 예정입니다. 필요한 도움을 준비할 수 있도록 간단히 응답해 주세요. 1회차에서 끝내지 못한 부분이 있어도 괜찮습니다.\n\n학생 이름·번호·평가 결과 등 실제 학생 정보와 비밀번호·API 키는 적지 말아 주세요.'
  );
  form.setCollectEmail(false);
  form.setConfirmationMessage('응답해 주셔서 감사합니다. 2회차 준비에 참고하겠습니다!');

  form.addMultipleChoiceItem()
    .setTitle('1회차에 어디까지 해 보셨나요?')
    .setHelpText('가장 마지막으로 해 본 단계를 골라 주세요.')
    .setChoiceValues([
      '앱 아이디어를 정리하거나 화면을 만들어 봤어요.',
      'GitHub에 코드를 저장했어요.',
      '인터넷 주소로 앱을 열어 봤어요.',
      '공개한 앱을 수정하고 다시 확인했어요.',
      '아직 시작하지 못했거나 진행 중이에요.',
      '잘 모르겠어요.',
      '1회차에 참여하지 못했어요.'
    ])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('2회차에 어떤 작업을 하고 싶으신가요?')
    .setHelpText('해당하는 것을 모두 골라 주세요.')
    .setChoiceValues([
      '1회차에 못 한 GitHub 저장·공개를 마무리하고 싶어요.',
      '만든 앱의 화면이나 기능을 고치고 싶어요.',
      '새로운 앱을 만들어 보고 싶어요.',
      'AI 에이전트가 앱을 고치는 과정을 보고 싶어요.',
      '개인정보와 공개할 때 주의할 점을 알고 싶어요.',
      '아직 정하지 못했어요.'
    ])
    .showOtherOption(true)
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('만들거나 고치고 싶은 앱이 있다면 간단히 알려 주세요.')
    .setHelpText('예: 가상의 번호를 사용하는 체크리스트, 퀴즈에 점수 표시하기. 실제 학생 정보는 적지 말아 주세요.')
    .setRequired(false);

  form.addCheckboxItem()
    .setTitle('2회차에서 특히 도움이 필요한 부분이 있나요?')
    .setHelpText('해당하는 것을 모두 골라 주세요.')
    .setChoiceValues([
      'AI에게 원하는 내용을 설명하기',
      '만든 코드 찾기와 복사하기',
      'GitHub에 저장하기',
      '인터넷 주소로 공개하기',
      '공개한 앱 수정하기',
      '개인정보와 데이터 저장 방식 이해하기',
      '아직 잘 모르겠어요.'
    ])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('1회차 진행 속도는 어떠셨나요?')
    .setChoiceValues(['빨랐어요.', '적당했어요.', '느렸어요.', '1회차에 참여하지 못했어요.'])
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('추가로 궁금한 점이나 바라는 점이 있나요?')
    .setHelpText('선택 사항입니다. 실제 학생 정보는 적지 말아 주세요.')
    .setRequired(false);

  console.log('설문 편집 주소: ' + form.getEditUrl());
  console.log('응답자에게 보낼 주소: ' + form.getPublishedUrl());
}
