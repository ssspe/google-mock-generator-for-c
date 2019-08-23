namespace EmbeddedCUnitTest {

	class MathsService
	{
	public:
		virtual ~MathsService() {} // Needed by std::unique_ptr
		MOCK_METHOD2(multiply, int(int, int)); // MOCK_METHODX, where X is number of inputs
	};
  
}
