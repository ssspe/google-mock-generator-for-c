#include "Mocks.h"

namespace EmbeddedCUnitTest {

	class TestFixture : public ::testing::Test
	{
  public:
		TestFixture() // Inits unique_ptr
		{
			_math.reset(new ::testing::NiceMock<MathsService>()); // Can use NiceMock, StrictMock or NaggyMock
    }
    
    ~TestFixture() // Destroys unique_ptr
		{
			_math.reset();
    }
    
    // Services
		static std::unique_ptr<MathsService> _math;
  };
  
}
