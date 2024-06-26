def tam_mot_linh_so_func(phone_number):
    tam_mot_linh_so = {
        0: "KHÔNG TỒN TẠI TRONG LINH SỐ",
        1: "(Quẻ Vạn tượng khởi thủy): Vũ trụ khởi nguyên, thiên địa khai thái, đại cát đại lợi, uy vọng trường thọ, kiện toàn phát đạt, thành tựu vĩ nghiệp. Người thường khó có thể nhận nổi. ĐẠI CÁT",
        2: "(Quẻ Hỗn độn ly loạn): Phá bại vất vả, khó thành sự nghiệp, vô mưu vô dũng, tiến thoái lưỡng nan. Như chim trong lồng, một bước khó đi, dễ vương bệnh tật. ĐẠI HUNG",
        3: "(Quẻ Danh lợi song thu): Âm dương hòa hợp, cát tường phúc hậu, là số thiên-địa-nhân vạn vật hình thành. Có điềm phát đạt, tài lộc dồi dào, đại lợi con cháu, gia vận. ĐẠI CÁT",
        4: "(Quẻ Phá hoại diệt liệt): Phân ly tang vong, rơi vào nghịch cảnh, tiến thoái lưỡng nan, bước vào suy thoái, đã hung càng hung, có điềm phát điên, tàn phế. Nhưng cũng thường sinh ra quái kiệt hoặc dị nhân. ĐẠI HUNG",
        5: "(Quẻ Phúc thọ song mỹ): Điềm âm dương giao hoan, hòa hợp, hoàn bích. Có vận thế thành công vĩ đại hoặc xây thành đại nghiệp ở đất khách, tất phải rời nơi sinh mới làm giầu được, kỵ dậm chân tại chỗ. ĐẠI CÁT",
        6: "(Quẻ Phú dụ bình an): Nhân tài đỉnh thịnh, gia vận hưng long, số này quá thịnh, thịnh quá thì sẽ suy, bề ngoài tốt đẹp, trong có ưu hoạn, cần ở yên nghĩ nguy, bình đạm hưởng thụ, vinh hoa nghĩ về lỗi lầm. CÁT",
        7: "(Quẻ Cương ngoan tuẫn mẫn): Có thế đại hùng lực, dũng cảm tiến lên giành thành công. Nhưng quá cương quá nóng vội sẽ ủ thành nội ngoại bất hòa. Con gái phải ôn hòa dưỡng đức mới lành. CÁT",
        8: "(Quẻ Kiên nghị khắc kỷ): Nhẫn nại khắc kỷ, tiến thủ tu thân thành đại nghiệp, ngoài cương trong cũng cương, sợ rằng đã thực hiện thì không thể dừng lại. Ý chí kiên cường, chỉ e sợ hiểm họa của trời. BÁN CÁT BÁN HUNG",
        9: "(Quẻ Bần khổ nghịch ác): Danh lợi đều không, cô độc khốn cùng, bất lợi cho gia vận, bất lợi cho quan hệ quyến thuộc, thậm chí bệnh nạn, kiện tụng, đoản mệnh. Nếu tam tài phối hợp tốt, có thể sinh ra cao tăng, triệu phú hoặc quái kiệt. HUNG",
        10: "(Quẻ Tử diệt hung ác): Là quẻ hung nhất, đại diện cho linh giới (địa ngục). Nhà tan cửa nát, quý khóc thần gào. Số đoản mệnh, bệnh tật, mất máu, tuyệt đối không được dùng. ĐẠI HUNG",
        11: "(Quẻ Vạn tượng canh tân): Dị quân đột khởi, âm dương điều hòa, tái hưng gia tộc, phồn vinh phú quý, tử tôn đẹp đẽ. Là điềm tốt toàn lực tiến công, phát triển thành công. ĐẠI CÁT",
        12: "(Quẻ Bạc nhược tỏa chiết): Người ngoài phản bội, người thân ly rời, lục thân duyên bạc, vật nuôi sinh sâu bọ, bất túc bất mãn, một mình tác chiến, trầm luân khổ nạn, vãn niên tối kỵ. HUNG",
        13: "(Quẻ Kỳ tài nghệ tinh): Sung mãn quỷ tài, thành công nhờ trí tuệ và kỹ nghệ, tự cho là thông minh, dễ rước bất hạnh, thuộc kỳ mưu kỳ lược. Quẻ này sinh quái kiệt. BÁN CÁT BÁN HUNG",
        14: "(Quẻ Phù trầm phá bại): Điềm phá gia, gia duyên rất bạc, có làm không có hưởng, nguy nạn liên miên, chết nơi đất khách, không có lợi khi ra khỏi nhà, điều kiện nhân quả tiên thiên kém tốt. HUNG",
        15: "(Quẻ Từ tường hữu đức): Phúc thọ viên mãn, hưng gia tụ tài, phú quý vinh hoa, được bề trên, bạn bè, cấp dưới ủng hộ. Có thể có được con cháu hiền thảo và tài phú. Tuổi vãn niên có phúc vô cùng. ĐẠI CÁT",
        16: "(Quẻ Trạch tâm nhân hậu): Là quẻ thủ lĩnh, ba đức tài, thọ, phúc đều đủ, tâm địa nhân hậu, có danh vọng, được quần chúng mến phục, thành tựu đại nghiệp. Hợp dùng cho cả nam nữ. CÁT",
        17: "(Quẻ Cương kiện bất khuất): Quyền uy cương cường, ý chí kiên định, khuyết thiếu hàm dưỡng, thiếu lòng bao dung, trong cương có nhu, hóa nguy thành an. Nữ giới dùng số này có chí khí anh hào. CÁT",
        18: "(Quẻ Chưởng quyền lợi đạt): Có trí mưu và quyền uy, thành công danh đạt, cố chấp chỉ biết mình, tự cho mình là đúng, khuyết thiếu hàm dưỡng, thiếu lòng bao dung. Nữ giới dùng cần phải phối hợp với bát tự, ngũ hành. CÁT",
        19: "(Quẻ Tỏa bại bất lợi): Quẻ đoản mệnh, bất lợi cho gia vận, tuy có trí tuệ, nhưng thường hay gặp hiểm nguy, rơi vào bệnh yếu, bị tàn phế, cô độc và đoản mệnh. Số này có thể sinh ra quái kiệt, triệu phú hoặc dị nhân. HUNG",
        20: "(Quẻ Phá diệt suy vong): Trăm sự không thành, tiến thoái lưỡng nan, khó được bình an, có tai họa máu chảy. Cũng là quẻ sướng trước khổ sau, tuyệt đối không thể dùng. ĐẠI HUNG",
        21: "(Quẻ Độc lập quyền uy): Số vận thủ lĩnh, được người tôn kính, hưởng tận vinh hoa phú quý. Như lầu cao vạn trượng, từ đất mà lên. Nữ giới dùng bất lợi cho nhân duyên, nếu dùng cần phối hợp với bát tự và ngũ hành. ĐẠI CÁT",
        22: "(Quẻ Thu thảo phùng sương): Kiếp đào hoa, họa vô đơn chí, tai nạn liên miên. Rơi vào cảnh ngộ bệnh nhược, khốn khổ. Nữ giới dùng tất khắc chồng khắc con. ĐẠI HUNG",
        23: "(Quẻ Tráng lệ quả cảm): Khí khái vĩ nhân, vận thế xung thiên, thành tựu đại nghiệp. Vì quá cương quá cường nên nữ giới dùng sẽ bất lợi cho nhân duyên, nếu dùng cần phối hợp với bát tự, ngũ hành. CÁT",
        24: "(Quẻ Kim tiền phong huệ): Tiền vào như nước, tay trắng làm nên, thành đại nghiệp, đắc đại tài, mạnh khỏe, danh dự, tài phú đều đủ cả. Quẻ này nam nữ dùng chung, đại lợi cho gia vận. ĐẠI CÁT",
        25: "(Quẻ Anh mại tuấn mẫn): Con gái xinh đẹp, con trai tuấn tú, có quý nhân khác giới giúp đỡ, trong nhu có cương, thành công phát đạt. Nhưng nói nhiều tất có sai lầm, hoặc tính cách cổ quái. CÁT",
        26: "(Quẻ Ba lan trùng điệt): Quát tháo ầm ĩ, biến quái kỳ dị, khổ nạn triền miên, tuy có lòng hiệp nghĩa, sát thân thành nhân. Quẻ này sinh anh hùng, vĩ nhân hoặc liệt sĩ (người có công oanh liệt). Nữ giới kỵ dùng số này. HUNG",
        27: "(Quẻ Tỏa bại trung chiết): Vì mất nhân duyên nên đứt gánh giữa đường, bị phỉ báng chịu nạn, phiền phức liên miên, vùi đi lấp lại, khó thành đại nghiệp. Rơi vào hình nạn, bệnh tật, u uất, cô độc và có khuynh hướng hiếu sắc. HUNG",
        28: "(Quẻ Họa loạn biệt ly): Vận gặp nạn, tuy có mệnh hào kiệt, cũng là anh hùng thất bại, bất lợi cho gia vận, cuối đời lao khổ, gia thuộc duyên bạc, có điềm thất hôn mất của. Nữ giới dùng số này tất bị cô quả. HUNG",
        29: "(Quẻ Quý trọng trí mưu): Gặp cát là cát, gặp hung chuyển hung. Mưu trí tiến thủ, tài lược tấu công, có tài lực quyền lực. Hành sự ngang ngạnh, lợn lành thành lợn què. Nữ giới dùng số này không có lợi cho nhân duyên. BÁN CÁT BÁN HUNG",
        30: "(Quẻ Phù trầm bất an): Quẻ thiên vận. Gặp cát gặp hung ở ngoại duyên. Bản thân chìm nổi vô định, thiện ác khó phân, lên voi xuống chó, đại thành đại bại, tất cả ở ngoại cảnh và ý trời. BÁN CÁT BÁN HUNG",
        31: "(Quẻ Hòa thuận viên mãn): Vận thủ lĩnh, nhân trí dũng đều đủ cả, vận may cát tường, ý chí kiên định, không hề dao động, thống lĩnh số đông, danh lợi song thu, phú quý vinh hoa. Nam nữ đều có thể dùng chung. ĐẠI CÁT",
        32: "(Quẻ Kiểu hạnh quý nhân): Như rồng bơi bến nước nông, chưa thành đại vận, nhưng may nhờ quý nhân đến giúp, sự nghiệp như ý, thế như chẻ tre, phẩm tính ôn lương, chỉ thiếu phần mạnh dạn, tiểu lợi thành nhân. CÁT",
        33: "(Quẻ Cương kiện quả đoán): Loan phượng gặp nhau, như rồng lên trời, gió mây gặp gỡ, danh nổi khắp thiên hạ. Quẻ này rất cứng rất nóng, vật cực tất phản, nữ giới không nên dùng, nếu dùng phải phối hợp với bát tự, ngũ hành. CÁT",
        34: "(Quẻ Phá gia vong thân): Là điềm ly loạn, phá hoại, bệnh yếu, thần kinh, đoản mệnh, họa máu rơi, cô độc khổ sở không người giúp đỡ, nhà tan cửa nát, thất bại lầm than, người thường không thể chịu nổi. ĐẠI HUNG",
        35: "(Quẻ Bảo thủ bình an): Vẻ đẹp nữ đức, ôn lương hòa thuận, trí đạt thành công. Nam giới dùng thì tư tưởng tiêu cực, thiếu đảm lượng khí phách, nếu dùng cần phải phối hợp với bát tự ngũ hành. Hợp nhất với nữ giới. CÁT",
        36: "(Quẻ Ba lan vạn trượng): Anh hùng hào kiệt, chìm nổi vạn trượng, quên mình thành nhân, không có lợi cho thương trường, chỉ hợp với chính trường. Làm người hào hiệp, trượng nghĩa, mạo hiểm thành công, phúc vận không dài. Nữ giới kỵ dùng số này. HUNG",
        37: "(Quẻ Từ tường trung thực): Độc lập quyền uy, phú quý trường thọ, thành thực được lòng người, vượt qua vạn khó khăn xây thành đại nghiệp, cuối cùng hưởng phú quý vô cùng. Cá tính cô độc ngạo nghễ, lưu ý hàm dưỡng đức hạnh để hưởng hạnh phúc. ĐẠI CÁT",
        38: "(Quẻ Bạc nhược bình phàm): Làm nghệ thuật thành công, nhưng thiếu uy vọng thống soái, khuyết tài năng thủ lĩnh, thất ý bạc nhược. Nếu phát triển mặt văn học, kỹ nghệ thì khá lý tưởng. BÁN HUNG BÁN CÁT",
        39: "(Quẻ Vinh hoa phú quý): Vận thủ lĩnh, quyền danh thọ lộc đều đủ cả, lại có thể truyền được cho con cháu. Vì quá cương quá nóng, nên nữ giới kỵ dùng, nếu dùng cần phải phối hợp với bát tự và ngũ hành. CÁT",
        40: "(Quẻ Phù trầm biến hóa): Giàu mưu lược, dũng cảm hơn người, thiếu uy vọng, phỉ báng công kích, thích mạo hiểm đem đến hung vận. Bệnh nhược, đoản mệnh, cô quả đều đến từ quẻ này. Nam nữ kỵ dùng. HUNG",
        41: "(Quẻ Kiện toàn hữu đức): Dương khí rất mạnh, có danh có lợi, khỏe mạnh trường thọ, thành tựu đại nghiệp. Quẻ này rất quý, lại có tâm niệm lên trên cầu tiến. Nam nữ đều nên dùng. ĐẠI CÁT",
        42: "(Quẻ Bác đạt đa năng): Là quẻ kỹ nghệ, nhiều nghề thông suốt, song mười nghề thì chín nghề không thành, trăm sự đều biết nhưng trăm sự đều không tinh thông. Gặp cát biến cát, gặp hung chuyển thành hung. Nếu phối hợp được bát tự, ngũ hành thì có thể dùng. BÁN CÁT BÁN HUNG",
        43: "(Quẻ Bạc nhược tán mạn): Là quẻ phá sản, tuy có tài hoa nhưng thiếu ý chí, bề ngoài thành công nhưng trong có mối thất bại, tán tài bất chính, tất rơi vào vòng hoang dâm, hung hiểm điệp trùng, không thể có kết quả cuối cùng tốt đẹp. HUNG",
        44: "(Quẻ Nghịch cảnh phiền muộn): Phá gia vong thân, sự thực không như mong muốn, vất vả thất bại. Quẻ này sinh quái kiệt, vĩ nhân, liệt sĩ (người có công oanh liệt) hoặc nhà phát minh. Nữ giới dùng tất rơi vào cô quả. ĐẠI HUNG",
        45: "(Quẻ Đức lượng hoành hậu): Thuận buồm xuôi gió, sáng nghiệp đại lợi, danh lợi song thu. Tuy nhiên không thể giữ được thành quả, sự nghiệp đến một giai đoạn thành công nào đó thì như mất lái giữa dòng, dễ rơi vào nguy nan. BÁN CÁT BÁN HUNG",
        46: "(Quẻ Tải bảo trầm châu): Biến quái kỳ diệu, như vào núi báu vật mà tay trắng ra về. Dù là người thành công may mắn cực đại cũng như thời khắc mùa xuân, cảnh đẹp không dài. Nữ giới dùng số này tất bị cô quả. HUNG",
        47: "(Quẻ Trinh tường cát khánh): Khai hoa kết quả, được quyền thế, tôn vinh, tài phú. Có thể tiến công lại có thể lùi về phòng thủ, hưởng thụ phúc huệ con cháu, là gia đình hạnh phúc. Nam nữ đều có thể dùng chung. ĐẠI CÁT",
        48: "(Quẻ Anh mại đức hậu): Là quẻ phẩm đức, làm cố vấn, thầy giáo là đại lợi. Có đầy trí mưu tài hoa, giúp người thành đại nghiệp, có đức có tín, tài thọ song toàn, hưởng thụ của cải trời cho. ĐẠI CÁT",
        49: "(Quẻ Biến quái thành nhân): Cát hung chiếm nửa, gặp cát là cát, gặp hung chuyển hung. Bản thân đứng ở núi cao, một thành một bại, chỉ nằm ở một đức một niệm mỏng manh. Nữ giới kỵ dùng số này. BÁN CÁT BÁN HUNG",
        50: "(Quẻ Cô quả ly sầu): Một thành một bại, sướng trước khổ sau, thê thảm vô cùng, gặp số hung tất tăng độ hung. Hình thương, cô quả, tai hại trùng điệp. Chỉ có tâm, đức, trí đoan chính mới có thể bù đắp. HUNG",
        51: "(Quẻ Phù trầm bất an): Một thịnh một suy, trong lúc thành công đột nhiên có hung biến, cuối đời chìm nổi bất an, khó thành đại nghiệp, lầu cao đổ gẫy, trong biển mất bạc. HUNG",
        52: "(Quẻ Trác thức đạt trí): Có sáng suốt cao kiến ban đầu cuối cùng thành đại nghiệp, danh lợi song thu. Duy có điều bất lợi về tình yêu. Người không thuận lợi về hôn nhân đa phần từ quẻ này mà ra. Nếu phối hợp tốt với bát tự, ngũ hành thì hôn nhân cũng không đáng ngại. CÁT",
        53: "(Quẻ Nạn khổ nội ưu): Tuy thành công nhất thời, nhưng sụp đổ nhanh chóng, không thể thành đại nghiệp một đời, trong cát có tàng đại hung, nửa đời phú quý, nửa đời tai họa, gặp hung càng hung, sẽ xảy ra nạn phá gia vong thân. HUNG",
        54: "(Quẻ Suy đồi vị đạt): Phá sản phá gia, bi thảm liên tục, bệnh tật, hình phạt, cô độc, đoản mệnh, chưa thành đại nghiệp đã đứt gánh giữa chừng. Quẻ này tuyệt không thể dùng. ĐẠI HUNG",
        55: "(Quẻ Ngoại vinh nội suy): Bề ngoài bóng bảy tốt lành, nhà giàu người nghèo, tâm thần bất định, tuy có hùng tâm tráng trí nhưng tự có hình thương, đại nghiệp khó thành. Nam nữ kỵ dùng. BÁN CÁT BÁN HUNG",
        56: "(Quẻ Hung bại bất lập): Vô dũng vô mưu, vạn sự khấp khểnh, bỏ dở giữa chừng, tổn thất tài sản, phá gia mất mạng, tâm thần bất an, tinh lực suy bại. Cần tu tâm tu đức mới mong có chuyển biến tốt đẹp. HUNG",
        57: "(Quẻ Thành tựu phạm hiểm): Trời ban hạnh phúc, cuối cùng thành đại nghiệp, số đại phú đại quý nhưng phải phạm một đại nạn mới có thể thành công. Trong lúc nguy nan có sự may mắn. Những việc thất đức chớ làm nếu không sẽ rước đại họa. CÁT",
        58: "(Quẻ Tiên khổ hậu cam): Trăm ngàn trở ngại, dị quân đột khởi, có đại tài nên giành đại thành công. Cuối đời vinh hiển, của cải dồi dào, đức tâm nhân hậu, nhân duyên tốt đẹp và thành công. CÁT",
        59: "(Quẻ Ý chí thoái bại): Ý chí bạc nhược mà thất chí thất bại, điều kiện tiên thiên đầy đủ nhưng thiếu khuyết đại hùng lực và nhân duyên, trầm luân hưởng lạc, có tính kiêu ngạo nên rước thất bại chỉ trong nháy mắt. Nữ giới dùng số này sẽ bị cô quả. HUNG",
        60: "(Quẻ Vô mưu thất câu): Là quẻ vô mưu, cô ý độc hành, lời ngay khó nghe, nhân duyên không tốt, bất lợi cho kinh doanh. Nhưng nhân tính bản chất lương thiện, thiếu lòng đức sẽ dễ rước quả báo xấu. HUNG",
        61: "(Quẻ Vinh hoa phồn đạt): Phồn hoa hưng thịnh, danh lợi song thu, của quý khắp nơi đổ về, cả đời phát đạt. Cẩn thận gia đình duyên bạc mà rước hiểm họa, cần tu tâm dưỡng đức, rèn tính bao dung thì sẽ được an. CÁT",
        62: "(Quẻ Tuyết thượng gia sương): Vô khí vô lực, sự việc không như mong muốn, chí nguyện khó đạt, bất lợi cho sự nghiệp, tai nạn liên miên. Nữ giới có số đào hoa, e là sẽ cô quả suốt đời. ĐẠI HUNG",
        63: "(Quẻ Phú đạt quý trọng): Là quẻ nhân quả tốt đẹp, vạn sự nhờ có thiên đức tưới nhuần mà thành đại nghiệp, có thể giành được phú quý danh dự. Nếu tiếp tục tích đức hành thiện thì con cháu tất hưng thịnh. ĐẠI CÁT",
        64: "(Quẻ Trầm muộn bình phàm): Như dập dềnh theo sóng cả, gặp nhiều giày vò, dẫn đến khuynh gia bại sản, cả đời khó được bình an vì một chữ “muộn”, rơi vào bệnh nạn, đoản mệnh, dâm loạn, thiệt đinh (mất con trai). ĐẠI HUNG",
        65: "(Quẻ Danh tài kiêm đắc): Vạn sự như ý, gia đình hưng thịnh, phúc thọ miên trường, hưởng tận vinh hoa, giống như có khí lành từ hướng Đông lại, thiên trường địa cửu. Con cháu gia tộc sau cũng được thơm lây. ĐẠI CÁT",
        66: "(Quẻ Thoái thủ tự tại): Trong ngoài bất hòa, tiến thoái lưỡng nan, khổ nạn liên miên. Nhưng quẻ này cũng hàm chứa trí đức, có thể thoái thủ, người tự biết vui vẻ bằng lòng với chính mình thì cũng có thể được hưởng phúc huệ. HUNG",
        67: "(Quẻ Tự ngã tăng tiến): Giống như leo cầu thang, từng bước lên cao, lập thân hưng gia, được cả danh lợi, tay trắng làm nên sự nghiệp lớn. Mạnh khỏe, danh dự, tài phú đều có, gia đình luôn vui vẻ. ĐẠI CÁT",
        68: "(Quẻ Bá khí thành nhân): Bẩm sinh thông minh dĩnh ngộ, có khí khái hào kiệt, rất có lợi cho việc sáng lập sự nghiệp. Duy có điều tính khí kiêu ngạo quá cao mà bị người ta đố kỵ, nhân duyên kém tốt. Quẻ này cũng có thể sinh ra hào kiệt, liệt sĩ (anh hùng) hoặc quái nhân. CÁT",
        69: "(Quẻ Trầm luân nan thành): Lục thân duyên bạc, bất túc bất mãn, rơi vào cảnh cô độc, chịu nghịch cảnh, ốm yếu, không thành sự nghiệp. Nếu như tam tài phối hợp không tốt dễ có tai nạn đột ngột. Đến tuổi trung niên, vãn niên dễ rơi vào cảnh chết trong cô quạnh. HUNG",
        70: "(Quẻ Phá diệt bại thân): Hung sát liên miên, trong lo ngoài lắng, vạn sự gập ghềnh. Có số ốm yếu, đoản mệnh, quan hình, chảy máu. Không thành công việc gì, số mệnh nhiều ách nạn. HUNG",
        71: "(Quẻ Cát hung tham bán): Tiến thoái lưỡng nan, cát hung khó lường, như rơi vào biển lớn, mênh mang sóng nước mà khó thoát. Gặp hung chuyển hung, gặp cát thì chuyển cát, trong lúc biến động khó mà kiểm soát. Chỉ có tu tâm dưỡng đức mới có thể cứu được. BÁN CÁT BÁN HUNG",
        72: "(Quẻ Ngoại tường trung hung): Tượng mây đen che lấp mặt trăng, nửa đời trước thì hạnh phúc, nửa đời sau thì bi thảm. Chết cũng giữ thể diện, bề ngoài phong quang, ngoài tươi trong héo. Nữ giới kỵ dùng số này. BÁN CÁT BÁN HUNG",
        73: "(Quẻ Chí đại tài sơ): Quyền uy thế trọng, chí lớn tài hèn, mắt cao tay thấp, hữu dũng vô mưu, tâm cao khí ngạo. Nhưng trời sinh có phúc nên có thể chớp cơ hội mà tạo chuyển biến tốt đẹp một thời. BÁN CÁT BÁN HUNG",
        74: "(Quẻ Trầm luân nghịch hại): Bất tài bất trí, trôi dạt theo gió, khuynh gia vong mạng, rơi vào bệnh nạn, đoản mệnh, dâm loạn, biến động liên miên. Nữ giới dùng số này tất cô quả hoặc mắc bệnh phụ khoa. ĐẠI HUNG",
        75: "(Quẻ Anh mại thoái an): Quẻ này sinh ra mỹ nữ tuấn nam, âm nhu hiển hiện, thiếu khí lực đại hùng cho nên bất lợi đối với sự nghiệp. Nên thoái thủ giữ mình, an hưởng thái bình, không được nóng nảy bộp chộp. CÁT",
        76: "(Quẻ Bệnh tai nạn ách): Là quẻ ác vận, tính kỳ quái, hung hiểm khốn khó, lên xuống thất thường, cả đời khó khăn. Quẻ này cũng có thể sinh ra quái kiệt, liệt sĩ (anh hùng). Nữ giới dùng số này sẽ bất lợi cho hôn nhân. HUNG",
        77: "(Quẻ Bán ưu bán hỷ): Số quái hào, gia đạo hưng thịnh, đột ngột rơi vào cô quả, nửa mừng nửa lo. Tài hoa cao ngạo, không ưa hư vinh, vui tại trong tâm, trong hung chứa cát, thịnh cực tất suy. Nữ giới kỵ dùng số này. BÁN CÁT BÁN HUNG",
        78: "(Quẻ Cần hành trí đạt): Túc trí đa mưu, thành bại được mất cũng trong giây lát. Như rơi vào sóng gió, không thể tự chủ. Gặp cát thì chuyển giàu, chuyển khỏe. Gặp hung thì khó thành. BÁN CÁT BÁN HUNG",
        79: "(Quẻ Nội ngoại khiếm tường): Quẻ quý nhân, thiếu tinh lực, chỉ vì có bệnh tật, bị phỉ báng, phong quang khó đến, ngạo khí khó thể hiện thì mới có quý nhân tương trợ, mới được tốt lành. HUNG",
        80: "(Quẻ Ba lan vạn trượng): Vạn sự gập ghềnh, hay gặp thất bại, hoảng hốt qua ngày. Quẻ này cũng có thể sinh ra quái kiệt, liệt sĩ (anh hùng), con có hiếu, liệt nữ…nhưng cũng đều là vận kém, ốm đau. HUNG",
        81: "(Quẻ Xuân phong di nhân): Là quẻ tôn quý nhất, vạn bảo đều quy tụ, nhuệ khí, danh dự, phúc đức tài đều có, may mắn tốt lành liên miên, thành tựu đại nghiệp, con cháu hưng thịnh, nam nữ đều có thể dùng chung. ĐẠI CÁT"
    }

    tam_mot_linh_so_rut_gon = {
        0: "KHÔNG TỒN TẠI",
        1: "ĐẠI CÁT",
        2: "ĐẠI HUNG",
        3: "ĐẠI CÁT",
        4: "ĐẠI HUNG",
        5: "ĐẠI CÁT",
        6: "CÁT",
        7: "CÁT",
        8: "BÁN CÁT BÁN HUNG",
        9: "HUNG",
        10: "ĐẠI HUNG",
        11: "ĐẠI CÁT",
        12: "HUNG",
        13: "BÁN CÁT BÁN HUNG",
        14: "HUNG",
        15: "ĐẠI CÁT",
        16: "CÁT",
        17: "CÁT",
        18: "CÁT",
        19: "HUNG",
        20: "ĐẠI HUNG",
        21: "ĐẠI CÁT",
        22: "ĐẠI HUNG",
        23: "CÁT",
        24: "ĐẠI CÁT",
        25: "CÁT",
        26: "HUNG",
        27: "HUNG",
        28: "HUNG",
        29: "BÁN CÁT BÁN HUNG",
        30: "BÁN CÁT BÁN HUNG",
        31: "ĐẠI CÁT",
        32: "CÁT",
        33: "CÁT",
        34: "ĐẠI HUNG",
        35: "CÁT",
        36: "HUNG",
        37: "ĐẠI CÁT",
        38: "BÁN HUNG BÁN CÁT",
        39: "CÁT",
        40: "HUNG",
        41: "ĐẠI CÁT",
        42: "BÁN CÁT BÁN HUNG",
        43: "HUNG",
        44: "ĐẠI HUNG",
        45: "BÁN CÁT BÁN HUNG",
        46: "HUNG",
        47: "ĐẠI CÁT",
        48: "ĐẠI CÁT",
        49: "BÁN CÁT BÁN HUNG",
        50: "HUNG",
        51: "HUNG",
        52: "CÁT",
        53: "HUNG",
        54: "ĐẠI HUNG",
        55: "BÁN CÁT BÁN HUNG",
        56: "HUNG",
        57: "CÁT",
        58: "CÁT",
        59: "HUNG",
        60: "HUNG",
        61: "CÁT",
        62: "ĐẠI HUNG",
        63: "ĐẠI CÁT",
        64: "ĐẠI HUNG",
        65: "ĐẠI CÁT",
        66: "HUNG",
        67: "ĐẠI CÁT",
        68: "CÁT",
        69: "HUNG",
        70: "HUNG",
        71: "BÁN CÁT BÁN HUNG",
        72: "BÁN CÁT BÁN HUNG",
        73: "BÁN CÁT BÁN HUNG",
        74: "ĐẠI HUNG",
        75: "CÁT",
        76: "HUNG",
        77: "BÁN CÁT BÁN HUNG",
        78: "BÁN CÁT BÁN HUNG",
        79: "HUNG",
        80: "HUNG",
        81: "ĐẠI CÁT"
    }

    # Lấy 4 số cuối
    # Kiểm tra xem số điện thoại có ít nhất 4 ký tự cuối là số không
    if not phone_number[-4:].isdigit():
        print("Số điện thoại không hợp lệ")
        exit()

    last_four_digits = int(phone_number[-4:])

    # Công thức tính linh số dựa trên 4 số cuối của số điện thoại

    # Chia cho 80
    division_result = last_four_digits / 80

    # Lấy phần nguyên và phần dư
    integer_part = int(division_result)
    fractional_part = division_result - integer_part

    # Nhân phần dư với 80 và làm tròn 2 chữ số để lấy linh số
    linh_so = int(round(fractional_part * 80, 2))

    dien_giai_linh_so = tam_mot_linh_so_rut_gon[linh_so]

    if "ĐẠI CÁT" in dien_giai_linh_so:
        print(f"Số điện thoại: {phone_number}. Quẻ số {linh_so}. {dien_giai_linh_so}")

phone_numbers_0 = [
    "0925288888", "0921455555", "0921588858", "0923858885", "0927626662", "0925669993",
    "0923958889", "0926925552", "0928802229", "0921823336", "0929888136", "0921999078",
    "0923622282", "0929383336", "0927599989", "0925266626", "0922599990", "0929388880",
    "0927855559", "0926666357", "0928188880", "0925899599", "0923966566", "0925633933",
    "0923166566", "0922322822", "0921599399", "0925122322", "0929955855", "0923898883",
    "0923068568", "0925968568", "0927568168", "0922368468", "0923668468", "0928468168",
    "0923927779", "0928855579", "0925111379", "0921221211", "0923939597", "0929968368",
    "0926168068", "0921968168", "0926522233", "0922533322", "0926111315", "0926181110",
    "0928211161", "0926111614", "0929111714", "0928111419", "0925959593", "0928181815",
    "0925959591", "0922555451", "0923595551", "0926222421", "0926565553", "0921255545",
    "0923122252", "0925111610", "0925511181", "0923299199", "0923336136", "0925899199",
    "0922999129", "0929247567",
    "0523666665", "0583333369", "0563333396", "0588888591", "0563222225", "0562222295",
    "0588888913", "0522222356", "0586666625", "0566666951", "0566666513", "0566666981",
    "0562222213", "0562111113", "0566666515", "0583000002", "0566666295", "0566666235",
    "0566666293", "0562333336", "0563222221", "0562222204", "0563333360", "0563333364",
    "0563333307", "0528888870", "0568888840", "0563333329", "0523333307", "0562222207",
    "0563333309", "0584444479", "0568888870", "0583333307", "0589999983", "0589000002",
    "0523000001", "0566666137", "0588888192", "0588888512", "0588888921", "0523000003",
    "0563000003", "0563222223", "0565111115", "0585111115", "0587111117", "0588222220",
    "0582222232", "0584444484", "0582888880", "0589999975", "0565555507", "0522222899",
    "0522222121", "0522222393", "0522222377", "0566666970", "0566666947", "0588888974",
    "0588888970", "0588888606", "0562222230", "0565555513", "0566666387", "0566666938",
    "0565000004", "0586000004", "0584999997", "0588888747", "0588888015", "0588888017",
    "0566666017", "0588885586", "0588622225", "0586666991", "0586666116", "0583933332",
    "0582555592", "0582222189", "0569999611", "0569999581", "0568888598", "0568888381",
    "0568888335", "0568888216", "0568233332", "0566669912", "0566665991", "0566662219",
    "0566662213", "0566288885", "0566122228", "0563822226", "0562222962", "0562211112",
    "0528366663", "0528222262", "0523333282", "0523199992", "0589999914", "0588888973",
    "0588888957", "0588888927", "0588888732", "0588888712", "0588888673", "0588888671",
    "0588888537", "0588888531", "0588888524", "0588888514", "0588888462", "0588888424",
    "0588888244", "0588888242", "0588888106", "0588888074", "0588888026", "0588888025",
    "0588888023", "0588888013", "0587777714", "0587777702", "0586888885", "0586666670",
    "0586666654", "0586666645", "0586444441", "0586222224", "0585555542", "0585555541",
    "0585555534", "0583333392", "0583333390", "0583333372", "0582222297", "0582222270",
    "0582222267", "0582222254", "0582222217", "0582222215", "0582222204", "0568888875",
    "0568888874", "0568888853", "0568888850", "0567777754", "0566666973", "0566666937",
    "0566666935", "0566666931", "0566666920", "0566666903", "0566666902", "0566666760",
    "0566666735", "0566666733", "0566666720", "0566666709", "0566666580", "0566666572",
    "0566666553", "0566666544", "0566666531", "0566666521", "0566666510", "0566666504",
    "0566666455", "0566666433", "0566666407", "0566666353", "0566666297", "0566666273",
    "0566666237", "0566666217", "0566666172", "0566666130", "0566666120", "0566666070",
    "0566666044", "0566666040", "0566666019", "0566666013", "0564111110", "0563333340",
    "0563333327", "0562888884", "0562222290", "0562222276", "0562222271", "0562222253",
    "0562222251", "0562222250", "0562222245", "0528888842", "0523333390", "0523333316",
    "0523333315", "0523333312", "0522222880", "0522222776", "0522222591", "0522222528",
    "0522222190", "0522222183", "0522222182", "0522222177", "0522222175", "0522222143"
]


phone_numbers_1 = [
    "0588228822", "0566446644", "0586223344", "0583886622", "0528998811", "0523335599",
    "0567224477", "0528113388", "0563223388", "0586337788", "0565228866", "0586113388",
    "0568007799", "0564889988", "0582995599", "0568338833", "0587993399", "0583882288",
    "0589993399", "0568992299", "0562995599", "0586990099", "0567662266", "0583662266",
    "0587799977", "0589556688", "0565006688", "0565922299", "0566447799", "0522115566",
    "0522995566", "0566228833", "0566885522", "0566881133", "0566882211", "0566881166",
    "0588998822", "0588227788", "0566882266", "0566558855", "0566552233", "0566551177",
    "0522779988", "0522442244", "0567777766", "0567008866", "0562998899", "0569667788",
    "0563662266", "0563226699", "0586223366", "0583223366", "0528996622", "0569668822",
    "0563668822", "0586213311", "0582989988", "0583333344", "0588779977", "0922119977",
    "0922770066", "0566448899", "0522997788", "0588115566", "0566559977", "0583888833",
    "0566000099", "0582999911", "0565333377", "0522666633", "0582777722", "0583999944",
    "0586444488", "0523555533", "0523999911", "0589117799", "0567447799", "0569007799",
    "0584447799", "0568447799"
]

phone_numbers_2 = [
    "0563628989", "0523882626", "0523992626", "0582259292", "0582255151", "0582322626",
    "0582611616", "0586239595", "0585638383", "0568222929", "0568999292", "0562168368",
    "0582168368", "0569868068", "0583168886", "0522663386", "0563138886", "0522918886",
    "0565551886", "0563889898", "0528153535", "0589992020", "0586665454", "0586662727",
    "0569995151", "0568885757", "0568882727", "0563999797", "0562999797", "0528999797",
    "0522999797"
]

phone_numbers_3 = [
    "0587878780", "0587878781", "0929255355", "0928988188", "0925988388", "0928566366",
    "0925222122", "0928533933", "0927566766", "0929266166", "0923933533", "0566444844",
    "0522522622", "0522522922", "0589888088", "0562888588", "0523666266", "0523399699",
    "0566566166", "0924331188", "0528228899", "0583668833", "0565223399", "0564557799",
    "0523226699", "0564337799", "0589113388", "0586669933", "0586113355", "0587007788",
    "0928822200", "0924992299", "0929778877", "0923553355", "0582889988", "0522299922",
    "0586992299", "0567661166", "0568558855", "0562889988", "0587990099", "0587669966",
    "0929168468", "0922468968", "0925368268", "0926368268", "0923668068", "0925468168",
    "0568368068", "0589168368", "0523168868", "0522068668", "0568068468", "0563768668",
    "0926966600", "0923211166", "0926033366", "0925733388", "0921633355", "0923433355",
    "0926122277", "0921233377", "0566255588", "0922213131", "0927774747", "0923339595",
    "0926999090", "0925551818", "0922236363", "0928111010", "0921119292", "0921115050",
    "0582229090", "0528999696", "0568883232", "0589998383", "0562228989", "0586665656",
    "0568884747", "0523338585", "0569992020", "0586662020", "0569990707", "0569990606",
    "0522122179", "0566166639", "0528885739", "0528882186", "0523999279", "0523999579",
    "0567899286", "0926822682", "0569196919", "0566662005", "0582088880", "0564088886",
    "0569999049", "0567898883", "0588880808", "0586506070", "0523368886", "0522000008",
    "0567118866", "0528828883", "0528888807", "0567895454", "0528333337", "0562989998",
    "0567838883", "0583333375", "0563968886", "0585168886", "0522485868", "0585456345",
    "0588888684", "0585345234", "0522488886", "0563633838", "0523989998", "0584567345",
    "0564567345", "0569888569", "0528066686", "0582066686", "0586117788", "0586068886",
    "0565117788", "0585117788", "0583068886", "0567008833", "0566515253", "0567889922",
    "0582086668", "0582998877", "0921158889", "0926518889", "0925638989", "0922518989",
    "0523898889", "0921082000", "0929234000", "0927500700", "0928765444", "0927779444",
    "0922020444", "0922011444", "0925130123", "0923288788", "0927988588", "0929550088",
    "0927770088", "0928538899", "0928208899", "0924048899", "0523868968", "0565989988",
    "0582323388", "0569997779", "0566660707", "0589999579", "0589583579", "0587393579",
    "0586953579"
]

phone_number = phone_numbers_0 + phone_numbers_1 + phone_numbers_2 + phone_numbers_3

for number in phone_number:
    tam_mot_linh_so_func(number)


